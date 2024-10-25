from django.db import models

# Create your models here.
class People(models.Model):
    Username=models.CharField(max_length=250)
    Email=models.EmailField(max_length=250)
    Password=models.CharField(max_length=250)



def __str__(self):
    return self.Username    




