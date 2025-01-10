from django.db import models

# Create your models here.
class contact(models.Model):
    email=models.CharField(max_length=40)
    password=models.CharField(max_length=30)  

    def __str__(self):
        return self.email