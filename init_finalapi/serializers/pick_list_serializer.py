from rest_framework import serializers
from init_finalapi.models import PickList

class PickListSerializer(serializers.ModelSerializer):
    """
    JSON Serializer for PickList
    """
    class Meta:
        model = PickList
        fields = (
            'id',
            'customer',
            'picked_by',
            'pick_list_date'
            )
        depth = 1
