from django.shortcuts import render
from django.views.generic import DetailView
from .models import Tshirt
from .forms import ProductOrderForm

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('2XL', '2 Extra Large')
)

# Create your views here.
def all_shirts(request):
    shirts = Tshirt.objects.all()
    return render(request, "shirts.html", {"shirts": shirts})
    

    
class ItemDetailView(DetailView):
    model = Tshirt