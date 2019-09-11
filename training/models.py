from django.db import models

# Create your models here.

class TrainingForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    phone_number = models.IntegerField()
    date = models.DateField()
    contacted = models.BooleanField(default=False)
    
    def __str__(self):
        return "{0} Training infomation request, submitted on {1}".format(self.name, self.date)
        