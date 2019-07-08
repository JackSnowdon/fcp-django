from django.shortcuts import get_object_or_404
from shop.models import *

def cart_contents(request):
    """
    Ensure anything that is added to the cart are availble when rendering 
    on everypage
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    for id, quantity in cart.items():
        """
        Below function will need to be adjusted when new shop models are 
        created
        """
        
        shirt = get_object_or_404(Tshirt, pk=id) 
        total += quantity * shirt.price
        product_count += quantity
        cart_items.append({'id':id, 'quantity':quantity, 'shirt':shirt })
        
    return { 'cart_items': cart_items, 'total': total, 'product_count': product_count }