from django import forms
from .models import Blog
from comments.models import Comment
from profiles.models import TypeOfFish, TypeOfFishing

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class BlogForm(forms.ModelForm):
    favourite_fish = forms.ModelChoiceField(queryset=TypeOfFish.objects.all(), required=False, label="Fish caught")
    favourite_fishing = forms.ModelChoiceField(queryset=TypeOfFishing.objects.all(), required=False, label="Fishing method used")

    class Meta:
        model = Blog
        fields = ['title', 'content', 'excerpt', 'featured_image', 'status', 'favourite_fish', 'favourite_fishing']