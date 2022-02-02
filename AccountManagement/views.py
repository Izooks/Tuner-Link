from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def register(request):
    form = UserCreationForm()
    return render(request, 'AccountManagement/register.html', {'form': form})