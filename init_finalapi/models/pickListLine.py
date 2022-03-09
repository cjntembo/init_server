from django.db import models

class PickListLine(models.Model):
    
    pick_list = models.ForeignKey("init_finalapi.pickList", on_delete=models.CASCADE, related_name="pick_list_lines")
    inventory = models.ForeignKey("init_finalapi.inventory", on_delete=models.CASCADE, related_name="pick_list_lines")
    qty_requested = models.IntegerField()