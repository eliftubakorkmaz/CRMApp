"""
URL configuration for CRMApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crm_app.views import *
from django.conf import settings
from user.views import *
from user.views import musteriler_listesi, add_customer, musteri_sil, musteri_duzenle, fırsatekle, fırsat_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', userLogin, name='login'),
    path('register/', userRegister, name='register'),
    path('musteriler/', musteriler_listesi, name='musteriler'),
    path('logout/', userLogout, name='logout'),
    path('create/', add_customer, name='create'),
    path('', index, name='index'),
    path('musteri/<int:musteri_id>/sil/', musteri_sil, name='musteri_sil'),
    path('musteri/<int:musteri_id>/duzenle/', musteri_duzenle, name='musteri_duzenle'),
    path('fırsatekle/', fırsatekle, name='fırsatekle'),
    path('fırsatlar/', fırsat_list, name='fırsatlar'),
]
