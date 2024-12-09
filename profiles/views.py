from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from allauth.account.views import SignupView  # Importing SignupView from AllAuth
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required

class CustomSignupView(SignupView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return redirect(reverse('profile_create'))  # Redirect to profile creation page

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'  # This allows you to reference the profile in the template

    def get_object(self, queryset=None):
        # Get the profile using slug from URL
        return get_object_or_404(Profile, slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        # Fetch default context data
        context = super().get_context_data(**kwargs)
        # Add blogs written by the user associated with the profile
        user = self.object.user  # The user linked to the profile
        context['blogs'] = user.blog_posts.filter(status=1)  # Fetch only published blogs
        return context

class ProfileCreateView(LoginRequiredMixin, CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_form.html'
    success_url = reverse_lazy('profile_detail')

    def form_valid(self, form):
        form.instance.user = self.request.user  # Associate the profile with the logged-in user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to profile detail using the newly created profile's slug
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile_edit.html'  # Use the new template
    success_url = '/profiles/'

    def get_success_url(self):
        return reverse_lazy('profile_detail', kwargs={'slug': self.object.slug})

    def get_object(self, queryset=None):
        # Override to get the profile for the logged-in user
        return get_object_or_404(Profile, user=self.request.user)

class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    template_name = 'profiles/profile_confirm_delete.html'
    success_url = reverse_lazy('home')  # Redirect after deletion; adjust as needed

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)





