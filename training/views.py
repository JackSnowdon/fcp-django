from django.shortcuts import render
from .forms import *

# Create your views here.
def training(request):
    """ Redeners traning """
    contact_form = ContactForm()
    return render(request, 'training.html', {'contact_form': contact_form})