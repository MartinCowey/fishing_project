from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels = {
            'body': '',  # This removes the label for the 'body' field
        }
        widgets = {
            'body': forms.Textarea(attrs={'placeholder': 'Enter your comment here...'})
        }