from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']