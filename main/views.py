from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='AccountManagement:login')
def home(request):
    return render(request, 'main/homepage.html')

def base(request):
    return render(request, 'main/base.html')