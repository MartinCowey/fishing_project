from django.urls import path
from . import views

urlpatterns = [
    path('add/<slug:slug>/', views.add_comment, name='add_comment'),
    path('<slug:slug>/edit_comment/<int:comment_id>/',
         views.comment_edit, name='comment_edit'),
]