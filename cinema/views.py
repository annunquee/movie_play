# cinema/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'cinema/home.html')

def about(request):
    return render(request, 'cinema/about.html')
