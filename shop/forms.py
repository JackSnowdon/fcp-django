from django import forms
from .models import Tshirt


class OrderForm(forms.ModelForm):
    class Meta: 
        model = Tshirt
        fields = '__all__'