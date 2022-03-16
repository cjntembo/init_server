from rest_framework import serializers
from init_finalapi.models import BinLocation

class BinLocationSerializer(serializers.ModelSerializer): 
    """
    JSON Serializer for BinLocation
    """
    class Meta:
        model = BinLocation
        fields = (
            'id',
            'bin_location_name',
            'binned_by'
            )
        depth = 1
