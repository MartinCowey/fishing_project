from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Blog
from comments.forms import CommentForm

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

def home_page(request):
    return render(request, 'home.html')  # This will render the home.html template


def blog_post(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    comments = blog.comments.filter(approved=True)
    comment_form = CommentForm()
    return render(request, 'blog/blog_post.html', {
        'blog': blog,
        'comments': comments,
        'comment_form': comment_form
    })

