from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .forms import CustomerForm
from .models import Musteri, Fırsat
from .forms import FırsatForm 


def index(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'register.html')

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

def add_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musteriler')
        
    context = {
        'form' : form
    }
    
    return render(request, 'create.html', context)

def musteriler_listesi(request):
    musteriler = Musteri.objects.all()
    return render(request, 'musteriler.html', {'musteriler': musteriler})

def musteri_sil(request, musteri_id):
    musteri = get_object_or_404(Musteri, id=musteri_id)
    if request.method == 'POST':
        musteri.delete()
        return redirect('musteriler')
    return render(request, 'musteri_sil.html', {'musteri': musteri})

def musteri_duzenle(request, musteri_id):
    musteri = get_object_or_404(Musteri, id=musteri_id)
    form = CustomerForm(instance=musteri)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=musteri)
        if form.is_valid():
            form.save()
            return redirect('musteriler')
    return render(request, 'musteri_duzenle.html', {'form': form})

def person_list(request):
    people = Person.objects.all()
    return render(request, 'person_list.html', {'people': people})

def fırsat_list(request):
    opportunities = Fırsat.objects.all()
    return render(request, 'fırsat_list.html', {'opportunities': opportunities})

def fırsat_list(request):
    opportunities = Fırsat.objects.all()
    return render(request, 'fırsat_list.html', {'opportunities': opportunities})

def fırsatekle(request):
    if request.method == 'POST':
        form = FırsatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fırsat_list')
    else:
        form = FırsatForm()

    return render(request, 'fırsatekle.html', {'form': form})