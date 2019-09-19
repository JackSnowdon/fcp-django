from django.test import TestCase
from django.urls import reverse
from .models import *

# Create your tests here.
class WrestlerTests(TestCase):
    """
    Tests to test Wrestler & Title Models
    """
    def test_wrestler_as_string(self):
        name = Wrestler(name='Pete Dunne')
        self.assertEqual(str(name), 'Pete Dunne')
        
    def test_title_as_a_string(self):
        title = Title(title_name='test', number_of_reigns='1')
        self.assertEqual(str(title), 'test x 1')
        
        
class RosterPageTests(TestCase):
    
    """
    Tests to check page is rendering with the correct template
    """

    def test_roster_page_status_code_and_path(self):
        response = self.client.get('/roster/')
        self.assertEquals(response.status_code, 200)

    def test_roster_page_url_name(self):
        response = self.client.get(reverse('roster'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_shop_uses_correct_template(self):
        response = self.client.get(reverse('roster'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'roster.html')
