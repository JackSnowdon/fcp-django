from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class TraingPageTests(TestCase):
    
    """
    Tests to check page is rendering with the correct template
    """

    def test_training_page_status_code_and_path(self):
        response = self.client.get('/training/')
        self.assertEquals(response.status_code, 200)

    def test_training_page_url_name(self):
        response = self.client.get(reverse('training'))
        self.assertEquals(response.status_code, 200)
       
        
    def test_training_uses_correct_template(self):
        response = self.client.get(reverse('training'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'training.html')
        
#    def test_post_a_training_request(self):
 #       respo