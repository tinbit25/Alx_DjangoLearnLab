# blog/views.py or blog/users/views.py
from django.shortcuts import render

def register(request):
    return render(request, 'users/register.html')

def login(request):
    return render(request, 'users/login.html')

def profile(request):
    return render(request, 'users/profile.html')
