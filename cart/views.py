from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """
    Renders full contents of the cart
    """
    return render(request, "cart.html")
    
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity      
    else:
        cart[id] = cart.get(id, quantity) 

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
    else:
        cart.pop(id)
        
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))