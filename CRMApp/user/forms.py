from typing import Any, Dict, Mapping, Optional, Type, Union
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django.forms.utils import ErrorList
from .models import *

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form_control'})
            field.help_text = ""

class CustomerForm(ModelForm):
    class Meta:
        model = Musteri
        fields = ['isim', 'soyisim', 'email', 'telefon', 'note']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
            field.help_text = ""

class Customer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class FırsatForm(ModelForm):
    class Meta:
        model = Fırsat
        fields = ['anlasma', 'asama', 'kapanis', 'durum']