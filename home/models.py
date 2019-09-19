from django.db import models

# Create your models here.

class BannerPost(models.Model):
    title = models.CharField(max_length=254, default='')
    description = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
        
"""
Used model below to display logo before learning how to store
static images on s3, left in for future use of different logos around website
"""
        
        
class Logo(models.Model):
    title = models.CharField(max_length=254, default='')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return self.title