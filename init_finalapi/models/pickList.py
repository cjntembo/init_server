from django.db import models

class PickList(models.Model):
    """PickList model"""
    customer = models.ForeignKey("init_finalapi.customer",
                                 on_delete=models.CASCADE,
                                 related_name="pick_lists")
    picked_by = models.ForeignKey("init_finalapi.employee",
                                  on_delete=models.CASCADE,
                                  related_name="pick_lists")
    pick_list_date = models.DateField(null=True)
