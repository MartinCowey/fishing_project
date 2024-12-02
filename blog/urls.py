from django.urls import path
from .views import BlogList, blog_post

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('<slug:slug>/', blog_post, name='blog_post'),
]