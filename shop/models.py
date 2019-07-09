from django.db import models

# Create your models here.

SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large')
)
    
class Tshirt(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    shirt_size = models.CharField(max_length=2, choices=SHIRT_SIZES)
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.name 


    