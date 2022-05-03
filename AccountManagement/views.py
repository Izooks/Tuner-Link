from email.mime import image
from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, logout
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
#this imports djangos pre built user creation form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from AccountManagement.decorators import unauthenticated_user
from .forms import CreateUserForm
from .forms import Profileform
from .decorators import  unauthenticated_user
from .models import *

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

@unauthenticated_user
def register_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            #Not sure if I should log the user in here or send them to the login
            return redirect('AccountManagement:login')
    else:
        form = CreateUserForm()

    context = {'form':form}
    return render(request, 'AccountManagement/register.html', {'form': form})

@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main:home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            
    context = {}
    return render(request, 'AccountManagement/login.html', context)

def logout_view(request):
    logout(request)
    return redirect('AccountManagement:login')

@login_required
def profile_view(request):
    info = Profile.objects.all()
    info_filter = info.filter(driver=request.user)
    return render(request, 'AccountManagement/profile.html', {'data': info_filter})

@login_required
def edit_view(request):
    if request.method == 'POST':
        form = forms.Profileform(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.driver = request.user
            instance.save()
            return redirect('AccountManagement:profile')
    else:
        form = forms.Profileform()
    return render(request, 'AccountManagement/edit.html', {'form': form})

def update_car(request, pk):
    update = Profile.objects.get(id=pk)
    form = forms.Profileform(instance=update)

    if request.method == 'POST':
        form = forms.Profileform(request.POST, instance=update)
        if form.is_valid():
            form.save()
            return redirect('AccountManagement:profile')

    return render(request, 'AccountManagement/update.html', {'form': form})

def delete_car(request, pk):
    update = Profile.objects.get(id=pk)
    if request.method == "POST":
        update.delete()
        return redirect('/')
    
    context = {'item': update}
    return render(request, 'AccountManagement/delete.html', context)

def search_view(request):

    if request.method == "POST":
        searched = request.POST['searched']
        builds = Profile.objects.filter(car__contains=searched)

        return render(request, 'AccountManagement/search.html', {'searched':searched, 'builds':builds})
    else:
        return render(request, 'AccountManagement/search.html', {})

    

