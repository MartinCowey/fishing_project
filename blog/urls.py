from django.urls import path
from .views import BlogList, BlogCreateView, blog_post, BlogSearchView

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('search/', BlogSearchView.as_view(), name='blog_search'),
    path('<slug:slug>/', blog_post, name='blog_post'),
    
]