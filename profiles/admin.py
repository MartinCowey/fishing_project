from django.contrib import admin
from .models import Profile  # Import your Profile model


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'bio', 'slug', 'favourite_fish', 'favourite_fishing'
    )  # Customize as needed
    search_fields = (
        'user__username', 'bio'
    )  # Enable searching by username or bio


# Alternatively, if you don't want to use a custom admin class:
# admin.site.register(Profile)
