from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PickListLine, Inventory

@receiver(post_save, sender=PickListLine)
def change_inv_count(sender, instance, created, **kwargs):
    """reduce qty_available if a qty_requested is added to a pickListLine"""

    if created:
        x = instance.inventory.qty_available
        y = sender.pickListLine.qty_requested

        total = (x-y)

        return total
    change_inv_count.save()
