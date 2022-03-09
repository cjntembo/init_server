from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Inventory(models.Model):

    description = models.CharField(max_length=150)
    unit_price = models.FloatField(validators=[
        MinValueValidator(0.00), MaxValueValidator(10000.00)])
    qty_available = models.IntegerField()
    bin_location = models.ForeignKey("init_finalapi.binlocation", on_delete=models.CASCADE, related_name="inventories")
    created_by = models.ForeignKey("init_finalapi.employee", on_delete=models.CASCADE, related_name="inventories")