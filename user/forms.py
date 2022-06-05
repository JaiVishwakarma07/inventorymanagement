from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    email = forms.EmailField()
    GSTIN = forms.CharField()

    class Meta:
        model = User
        fields = ['username','email','GSTIN','password1','password2']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address','phone','gstin','image']

