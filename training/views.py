from django.shortcuts import redirect, render, reverse
from django.contrib import messages
from django.utils import timezone
from .forms import *

# Create your views here.
def training(request):
    """ Redeners Training page and sends contact_form if post  """
    if request.method=="POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            form = contact_form.save(commit=False)
            form.date = timezone.now()
            messages.error(request, "Infomation request sent, we will be in contact soon!")
            form.save()
            return redirect(reverse('index'))
        else: 
            messages.error(request, "fail")
    else:
        contact_form = ContactForm()
        return render(request, 'training.html', {'contact_form': contact_form})
        
