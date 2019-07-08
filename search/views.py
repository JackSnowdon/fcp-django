from django.shortcuts import render
from shop.models import Tshirt

# Create your views here.

def do_search(request):
    products = Tshirt.objects.filter(name__icontains=request.GET['q'])
    return render(request, "shirts.html", {"products": products})