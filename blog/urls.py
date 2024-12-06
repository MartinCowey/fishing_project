from django.urls import path
from .views import BlogList, blog_post, BlogSearchView

urlpatterns = [
    path('', BlogList.as_view(), name='blog_list'),
    path('search/', BlogSearchView.as_view(), name='blog_search'),
    path('<slug:slug>/', blog_post, name='blog_post'),
    
]