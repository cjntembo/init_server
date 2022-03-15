from rest_framework import serializers
from init_finalapi.models import Employee

class EmployeeSerializer(serializers.ModelSerializer): 
    """
    JSON Serializer for Employee
    """
    class Meta:
        model = Employee
        fields = (
            'id',
            'hire_date',
            'birth_date',
            'address',
            'city',
            'state',
            'postal_code',
            'country',
            'phone_number'
            )
        depth = 1
