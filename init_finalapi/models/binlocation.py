from django.db import models


class BinLocation(models.Model):
    
    bin_location_name = models.CharField(max_length=50)
    binned_by = models.ForeignKey("init_finalapi.employee", on_delete=models.CASCADE, related_name="bin_locations")