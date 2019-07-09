from django import forms
from django.forms import ModelForm
from .models import Tshirt


class OrderForm(ModelForm):
    class Meta: 
        model = Tshirt
        fields = '__all__'