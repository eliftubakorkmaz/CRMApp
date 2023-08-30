from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout

def musteriler(request):
    return render(request, 'musteriler.html')

def userRegister(request):
    form = UserForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
        
    context = {
        'form' : form
    }
    return render(request, 'register.html', context)

def userLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('musteriler')
        else:
            return redirect('index')
    return render(request, 'index.html')
        
def userLogout(request):
    logout(request)
    return redirect('index')