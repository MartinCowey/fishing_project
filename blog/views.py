from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Blog, TypeOfFish, TypeOfFishing
from .forms import CommentForm, BlogForm
from comments.forms import CommentForm
from django.contrib import messages
from profiles.models import Profile
from django.utils.text import slugify

# Create your views here.


class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name = 'base.html'


class BlogSearchView(ListView):
    model = Blog
    template_name = 'blog/blog_search.html'
    context_object_name = 'blogs'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        fish_type = self.request.GET.get('fish')
        fishing_method = self.request.GET.get('method')

        queryset = Blog.objects.filter(status=1)

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(author__username__icontains=query)
            )

        if fish_type:
            queryset = queryset.filter(favourite_fish__name=fish_type)

        if fishing_method:
            queryset = queryset.filter(favourite_fishing__name=fishing_method)

        return queryset.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fish_types'] = TypeOfFish.objects.all()
        context['fishing_methods'] = TypeOfFishing.objects.all()
        return context


class BlogList(ListView):
    queryset = Blog.objects.filter(status=1)
    template_name = "blog/blog_list.html"
    paginate_by = 6
    context_object_name = 'blogs'


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

    # Add a blog post
    def dispatch(self, request, *args, **kwargs):
        # Ensure the user has a profile
        if not Profile.objects.filter(user=request.user).exists():
            messages.error(
                request,
                "It's like fishing at the wrong depth! You need to"
                " create a profile to add a blog post."
            )
            return redirect('profile_create')
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.initial['excerpt'] = 'Fished It, Mate'
        form.initial['status'] = 1
        return form

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.cleaned_data['title'])
        if not form.instance.excerpt:
            form.instance.excerpt = form.instance.content[:100] + '...'
        messages.success(
            self.request,
            "Your blog post was created successfully!"
        )
        return super().form_valid(form)


class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        if not form.initial.get('excerpt'):
            form.initial['excerpt'] = 'Fished It, Mate'
        if not form.initial.get('status'):
            form.initial['status'] = 1  # Assuming 1 is for 'Published'
        return form

    def form_valid(self, form):
        messages.success(
            self.request, "Your blog post was updated successfully!"
        )
        return super().form_valid(form)


def home_page(request):
    return render(request, 'home.html')  # This will render home.html template


def blog_post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.all().order_by("-created_on")
    comment_count = blog.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(request, 'blog/blog_post.html', {
        'blog': blog,
        'blog_slug': blog.slug,
        'comments': comments,
        'comment_form': comment_form,
        'comment_count': comment_count,
    })


# Edit view
def blog_edit(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Ensure that the logged-in user is the author of the blog
    if blog.author != request.user:
        return HttpResponseForbidden(
            "You're fishing in the wrong place... You do not have permission"
            " to edit this post."
        )

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your blog post was updated successfully!"
            )
            return redirect('blog_post', slug=blog.slug)
    else:
        form = BlogForm(instance=blog)

    return render(request, 'blog/blog_edit.html', {'form': form, 'blog': blog})


# Delete view
def blog_delete(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    # Ensure that the logged-in user is the author of the blog
    if blog.author != request.user:
        return HttpResponseForbidden(
            "You're fishing in the wrong place... You do not have permission"
            " to delete this post."
        )

    if request.method == 'POST':
        blog.delete()
        messages.success(request, "Your blog post was deleted successfully.")
        return redirect('blog_list')

    return render(request, 'blog/blog_delete.html', {'blog': blog})
