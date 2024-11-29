from . import views
from django.urls import path

urlpatterns = [ 
    path('', views.blog_list, name='blog_list'),  # This will show the list of blogs at /blog/
    path('<slug:slug>/', views.blog_post, name='blog_post'),  # This will show individual blog posts
]
