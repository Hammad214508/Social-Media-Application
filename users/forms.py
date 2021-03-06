from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()#required=False
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Update the user's profile
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()#required=False so that the user can submit the form with the email being blank
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
