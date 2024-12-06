from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Blog, TypeOfFish, TypeOfFishing
from .forms import CommentForm, BlogForm
from comments.forms import CommentForm
from django.contrib import messages

# Create your views here.

class HomePage(TemplateView): 
    """
    Displays home page"
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
        context['fish_types'] = TypeOfFish.objects.all()  # Fetch all fish types
        context['fishing_methods'] = TypeOfFishing.objects.all()  # Fetch all fishing methods
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

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')

def home_page(request):
    return render(request, 'home.html')  # This will render the home.html template


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
                request, messages.SUCCESS,
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
