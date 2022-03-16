from rest_framework import serializers
from init_finalapi.models import Inventory

class InventorySerializer(serializers.ModelSerializer): 
    """
    JSON Serializer for Inventory
    """
    class Meta:
        model = Inventory
        fields = (
            'id',
            'description',
            'unit_price',
            'qty_available',
            'bin_location',
            'created_by'
            )
        depth = 1
