from django.urls import path
from . import views
from .views import BlogList, BlogCreateView, blog_post, BlogSearchView, blog_edit, blog_delete 

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<slug:slug>/edit/', views.blog_edit, name='blog_edit'),
    path('blog/<slug:slug>/delete/', views.blog_delete, name='blog_delete'),
    path('search/', BlogSearchView.as_view(), name='blog_search'),
    path('<slug:slug>/', blog_post, name='blog_post'),
    
]
