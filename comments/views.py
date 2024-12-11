from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import Comment
from blog.models import Blog
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib import messages


def add_comment(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.blog = blog
            comment.save()
    return redirect('blog_post', slug=blog.slug)


def comment_edit(request, slug, comment_id):
    """
    View to edit comments.
    """
    if request.method == "POST":
        queryset = Blog.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, 'Comment Updated!'
            )
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
            )

    return HttpResponseRedirect(reverse('blog_post', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete a comment.
    """
    queryset = Blog.objects.filter(status=1)
    blog = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted!'
        )
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!'
        )

    return HttpResponseRedirect(reverse('blog_post', args=[slug]))
