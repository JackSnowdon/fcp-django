from django.test import TestCase
from .views import *

# Create your tests here.

class HomePageTests(TestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        
    def test_home_uses_correct_template(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        
    def test_home_page_contains_correct_html_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<title>Fight Club: Pro</title>')