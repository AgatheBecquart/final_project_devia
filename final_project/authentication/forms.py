from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class SignUpForm(UserCreationForm):
    # Add any additional fields you want in the signup form
    class Meta:
        model = CustomUser
        fields = ('username', 'email')
