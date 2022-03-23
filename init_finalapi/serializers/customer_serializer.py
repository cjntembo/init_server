from rest_framework import serializers
from init_finalapi.models import Customer

class CustomerSerializer(serializers.ModelSerializer): 
    """
    JSON Serializer for Customer
    """
    class Meta:
        model = Customer
        fields = (
            'id',
            'first_name',
            'last_name',
            'company',
            'email',
            'address',
            'city',
            'state',
            'postal_code',
            'country',
            # 'phone_number',
            # 'employee'
            )
        depth = 1
