from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, logout

#this imports djangos pre built user creation form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            #Not sure if I should log the user in here or send them to the login
            return redirect('AccountManagement:login')
    else:
        form = UserCreationForm()
    return render(request, 'AccountManagement/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in the user
            user=form.get_user()
            login(request, user)
            return redirect('main:home')
    else:
        form = AuthenticationForm()
    return render(request, 'AccountManagement/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('AccountManagement:login')