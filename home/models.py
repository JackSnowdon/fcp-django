from django.db import models

# Create your models here.

class BannerPost(models.Model):
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
        
class Logo(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title