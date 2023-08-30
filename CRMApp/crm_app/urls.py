from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('create/', views.add_customer, name='create'),
    path('musteriler/', views.musteriler_listesi, name='musteriler'),
] 