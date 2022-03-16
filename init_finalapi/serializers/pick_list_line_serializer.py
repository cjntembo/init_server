from rest_framework import serializers
from init_finalapi.models import PickListLine

class PickListLineSerializer(serializers.ModelSerializer):
    """
    JSON Serializer for PickListLine
    """
    class Meta:
        model = PickListLine
        fields = (
            'id',
            'pick_list',
            'inventory',
            'qty_requested'
            )
        depth = 1
