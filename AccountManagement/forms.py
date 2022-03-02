from pyexpat import model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User 
from .models import Profile
from django.forms import ModelForm

from AccountManagement import models



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class Profileform(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = ['city', 'image', 'car', 'description', 'modifications']