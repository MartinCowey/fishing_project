from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from django.shortcuts import redirect
from django.urls import reverse


@receiver(user_signed_up)
def create_profile(sender, request, user, **kwargs):
    # Redirect to profile creation page after signup
    return redirect(reverse('profile_create'))
