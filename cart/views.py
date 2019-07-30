from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.

def view_cart(request):
    """
    Renders full contents of the cart
    """
    return render(request, "cart.html")

def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = 1
    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity 
    else:
        cart[id] = cart.get(id, quantity) 
    
    messages.success(request, "You have successfully added the item to your cart!")
    request.session['cart'] = cart
    return redirect(reverse('shirts'))
    
def adjust_cart(request, id):
    """
    Adjust the quantity of the specifed product in the cart
    """
    quantity=int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})
    
    if quantity > 0:
        cart[id] = quantity
        messages.success(request, "You have adjusted the item in your cart!")
    else:
        cart.pop(id)
        messages.success(request, "You have removed the item in your cart!")

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))