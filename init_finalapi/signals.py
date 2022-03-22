from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PickListLine

# @receiver(post_save, sender=PickListLine)
# def change_inv_count(sender, instance, created, **kwargs):
#     """reduce qty_available if a qty_requested is added to a pickListLine"""

#     if created:
#         x = instance.inventory.qty_available
#         y = sender.pickListLine.qty_requested

#         new_qty_available = (x-y)

#         return new_qty_available
#     change_inv_count.save()

@receiver(post_save, sender=PickListLine, dispatch_uid="update_inv_count")
def update_inv_count(sender, instance, created, **kwargs):
    """reduce qty_available if a qty_requested is added to a pickListLine
        Method for updating
    """
    if created:
        instance.inventory.qty_available -= instance.qty_requested
        instance.inventory.save()
