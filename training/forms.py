from django import forms
from .models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = TrainingForm
        exclude = ['date', 'contacted', 'phone_nummer']