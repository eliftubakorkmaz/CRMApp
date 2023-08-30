from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def musteriler(request):
    return render(request, 'musteriler.html')

def register(request):
    return render(request, 'register.html')