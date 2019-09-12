from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class WrestlerTests(TestCase):
    """
    Tests to test Wrestler Shop Model
    """
    def test_wrestler_model(self):
        name = Wrestler(name='Pete Dunne')
        birthplace = Wrestler(birthplace='Birmingham, UK')
        self.assertEqual(str(name), 'Pete Dunne')
        self.assertEqual(str(birthplace), 'Birmingham, UK')
        
        
class RosterPageTests(TestCase):
    
    """
    Tests to check page is rendering with the correct template
    """

    def test_roster_page_status_code(self):
        response = self.client.get(reverse('roster'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_shop_uses_correct_template(self):
        response = self.client.get(reverse('roster'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'roster.html')
