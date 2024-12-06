from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Blog
from .forms import CommentForm, BlogForm
from comments.forms import CommentForm
from django.contrib import messages

# Create your views here.

class HomePage(TemplateView): 
    """
    Displays home page"
    """
    template_name = 'base.html'


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
