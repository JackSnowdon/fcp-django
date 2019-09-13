from django.test import TestCase
from django.shortcuts import render, reverse

# Create your tests here.

class CartPageTests(TestCase):
    
    """
    Tests for cart page rendering
    """
    
    def test_cart_page_status_code_and_path(self):
        response = self.client.get('/cart/')
        self.assertEquals(response.status_code, 200)
        
    def test_cart_page_url_name(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_cart_uses_correct_template(self):
        response = self.client.get(reverse('view_cart'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart.html')