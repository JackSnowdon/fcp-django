from django.db import models

# Create your models here.

FCP = 'FCP'
Schadenfreude = 'Schadenfreude'
    
alignment_choices = (
    (Schadenfreude, 'Schadenfreude'),
    (FCP, 'Fight Club: Pro'),
)

class Title(models.Model):
    title_name = models.CharField(max_length=30)
    number_of_reigns = models.IntegerField()

    def __str__(self):
        return '{0} x {1}'.format(self.title_name, self.number_of_reigns)
        

class Wrestler(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    description = models.TextField()
    alignment = models.CharField(max_length=32, choices=alignment_choices, default=FCP)
    titles = models.ManyToManyField(Title)
    
    def __str__(self):
        return self.name
