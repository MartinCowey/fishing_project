from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from .models import Comment
from blog.models import Blog
from .forms import CommentForm

def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = blog
            comment.save()
            return redirect('blog_detail', slug=blog.slug)
    return redirect('blog_detail', slug=blog.slug)