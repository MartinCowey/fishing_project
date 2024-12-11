from django.urls import path
from .views import (
    ProfileDetailView,
    ProfileUpdateView,
    ProfileCreateView,
    ProfileDeleteView,
    CustomSignupView,
)
from . import views  # Import the views module

urlpatterns = [
    path(
        'signup/',
        CustomSignupView.as_view(),
        name='account_signup',
    ),  # Use custom signup view here
    path(
        'create/',
        ProfileCreateView.as_view(),
        name='profile_create',
    ),
    path(
        '<slug:slug>/',
        ProfileDetailView.as_view(),
        name='profile_detail',
    ),
    path(
        'profiles/<slug:slug>/edit/',
        ProfileUpdateView.as_view(),
        name='profile_edit',
    ),
    path(
        '<slug:slug>/delete/',
        ProfileDeleteView.as_view(),
        name='profile_delete',
    ),
]
