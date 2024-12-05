from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'
    context_object_name = 'profile'  # This allows you to reference the profile in the template

    def get_object(self, queryset=None):
        # Get the profile using slug from URL
        return get_object_or_404(Profile, slug=self.kwargs['slug'])

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





