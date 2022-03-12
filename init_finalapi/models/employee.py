from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Employee(models.Model):
    """_summary_

    employees model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=55, default="enter email here")
    hire_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    postal_code = models.IntegerField(null=True)
    country = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=14, null=True)