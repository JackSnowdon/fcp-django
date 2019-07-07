from django.shortcuts import render
from .models import Tshirt



# Create your views here.
def all_shirts(request):
    shirts = Tshirt.objects.all()
    return render(request, "shirts.html", {"shirts": shirts})