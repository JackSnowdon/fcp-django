from django.shortcuts import render
from .models import Tshirt
from .forms import OrderForm

# Create your views here.
def all_shirts(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            shirts = Tshirt.objects.all()
            
    else:
        shirts = Tshirt.objects.all()
        return render(request, "shirts.html", {"shirts": shirts})