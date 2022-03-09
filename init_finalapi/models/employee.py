from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Employee(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hire_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(auto_now_add=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=14)