from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

# Create your views here.

def all_roster(request):
    # Gets all Wrestler objects and orders alphabetically 
    roster = Wrestler.objects.order_by('name')
    # Then splits ordered objects by alignment_choice lists
    fcp = roster.filter(alignment='FCP')
    schadenfreude = roster.filter(alignment='Schadenfreude')
    return render(request, "roster.html", {"fcp": fcp, "schadenfreude":schadenfreude})
    
class SingleWrestler(DetailView):
    model = Wrestler