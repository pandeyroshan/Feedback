from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=12)
    review=models.CharField(max_length=300)

    
