from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class TshirtTests(TestCase):
    """
    Tests to test Tshirt Shop Model
    """
    def test_tshirt_name(self):
        test_name = Tshirt(name='A Shirt')
        self.assertEqual(str(test_name), 'A Shirt')
        
        
class ShopPageTests(TestCase):
    
    """
    Tests to check page is rendering with the correct template
    """
    
    def test_shop_page_status_code_and_path(self):
        response = self.client.get('/shop/')
        self.assertEquals(response.status_code, 200)

    def test_shop_page_url_name(self):
        response = self.client.get(reverse('shirts'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_shop_uses_correct_template(self):
        response = self.client.get(reverse('shirts'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'shirts.html')
