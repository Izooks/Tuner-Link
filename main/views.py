from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from AccountManagement.models import Profile
from .models import *

# Create your views here.

@login_required(login_url='AccountManagement:login')
def home(request):
    content = Profile.objects.all()
    return render(request, 'main/homepage.html', {'test': content})

def base(request):
    return render(request, 'main/base.html')

def build_view(request, pk):
    user = Profile.objects.get(id=pk)
    return render(request, 'main/build.html', {'test': user})