from django.shortcuts import render

def home(request):
    return render(request, 'crm_app/index.html')
