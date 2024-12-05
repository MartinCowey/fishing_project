from django.urls import path
from .views import ProfileDetailView, ProfileUpdateView, ProfileCreateView, ProfileDeleteView

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profiles/<slug:slug>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('<slug:slug>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]
