from django.test import TestCase
from .models import *

# Create your tests here.
class TshirtTests(TestCase):
    """
    Tests to test Tshirt Shop Model
    """
    def test_str(self):
        test_name = Tshirt(name='A Shirt')
        self.assertEqual(str(test_name), 'A Shirt')
        