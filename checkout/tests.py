from django.test import TestCase
from django.shortcuts import render, reverse
from django.contrib.auth.models import User

# Create your tests here.

class CheckoutPageTests(TestCase):
    
    """
    Tests for checkout page rendering
    """
    
    def setUp(self):
        self.user = User.objects.create_user(username='test',
                                        password='testword')
        self.client.login(username='test', password='testword')
    
    def test_checkout_page_status_code_and_path(self):
        response = self.client.get('/checkout/')
        self.assertEquals(response.status_code, 200)
        
    def test_checkout_page_url_name(self):
        response = self.client.get(reverse('checkout'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_checkout_uses_correct_template(self):
        response = self.client.get(reverse('checkout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout.html')