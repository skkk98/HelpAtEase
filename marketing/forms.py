from django.contrib.auth.models import User
from django import forms
from .models import Type

class RegisterForm(forms.Form):
    CHOICES = (
        ('Volunteer', 'VOLUNTEER'),
        ('Ngo', 'NGO'),
        ('Funder', 'FUNDER'),
    )
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=200, help_text='Required')
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    Register_As = forms.CharField(widget=forms.Select(choices=CHOICES))
    class Meta:
        model = User, Type
        fields = ['username', 'email', 'password', 'confirm_password', 'Register_As']

class LoginForm(forms.Form):
    CHOICES = (
        ('Volunteer', 'VOLUNTEER'),
        ('Ngo', 'NGO'),
        ('Funder', 'FUNDER'),
    )
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
    Register_As = forms.CharField(widget=forms.Select(choices=CHOICES))
    class Meta:
        model = User, Type
        fields = ['username', 'password', 'Register_As']