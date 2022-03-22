from django.db import models

class Customer(models.Model):
    """
    customer model
    """
    first_name = models.CharField(max_length=55)
    last_name = models.CharField(max_length=55)
    company = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=50)
    email = models.EmailField(max_length=55)
    employee = models.ForeignKey("init_finalapi.employee", on_delete=models.CASCADE, related_name="customers", null=True)