from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class LoginForm(AuthenticationForm):
    """
      Form for Logging in  users
    """
    email  = forms.CharField(label= 'Password', widget=forms.TextInput)



class registerForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "mobile_no"]