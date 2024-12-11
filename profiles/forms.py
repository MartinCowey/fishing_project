from django import forms
from .models import Profile, TypeOfFishing, TypeOfFish


class ProfileForm(forms.ModelForm):
    favourite_fish = forms.ModelChoiceField(
        queryset=TypeOfFish.objects.all(),
        widget=forms.Select,
    )
    favourite_fishing = forms.ModelChoiceField(
        queryset=TypeOfFishing.objects.all(),
        widget=forms.Select,
    )

    class Meta:
        model = Profile
        fields = ['bio', 'profile_pic', 'favourite_fish', 'favourite_fishing']
