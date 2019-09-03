from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

# Create your views here.

def all_roster(request):
    roster = Wrestler.objects.all()
    fcp = roster.filter(alignment__align='FCP')
    schadenfreude = roster.filter(alignment__align='Schadenfreude')
    return render(request, "roster.html", {"fcp": fcp, "schadenfreude":schadenfreude})
    
class SingleWrestler(DetailView):
    model = Wrestler