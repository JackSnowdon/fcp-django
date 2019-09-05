from django import forms
from .models import Tshirt

class ProductOrderForm(forms.ModelForm):
    class Meta: 
        model = Tshirt
        fields = '__all__'