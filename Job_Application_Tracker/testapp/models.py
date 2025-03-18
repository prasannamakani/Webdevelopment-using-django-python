from django.db import models
from django.utils.timezone import now

# Create your models here.
class People(models.Model):
    Username=models.CharField(max_length=250)
    Password=models.CharField(max_length=250)
    Confirm_Password=models.CharField(max_length=250)

    def __str__(self):
        return self.Username    






class JobApplication(models.Model):
    Company = models.CharField(max_length=255)
    Position = models.CharField(max_length=255)
    Ctc = models.PositiveIntegerField(null=True , blank=True )
    Date = models.DateField(default=now)

    def __str__(self):
        return f"{self.Company} - {self.Position}"
