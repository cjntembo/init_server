"""View module for handling requests about employees"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from init_finalapi.models import Employee
from init_finalapi.serializers.employee_serializer import EmployeeSerializer

class EmployeeView(ViewSet):
    """Init Employees"""
    def retrieve(self, request, pk=None):
        """Handle Get Requests for single Employee
        Returns --JSON serialized employee
        """
        try:
            employee = Employee.objects.get(pk=pk)
            serializer = EmployeeSerializer(employee, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Gets all Employees"""
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True, context={'request': request})
        return Response(serializer.data)

    # @permission_classes([IsAdminUser])
    def create(self, request):
        """Handle Post Operations
        Returns:
        Response -- JSON serialized an employee instance
        """
        if not request.auth.user.is_staff:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        employee = Employee()
        employee.birth_date = request.data["birth_date"]
        employee.address = request.data['address']
        employee.city = request.data['city']
        employee.state = request.data['state']
        employee.postal_code = request.data['postal_code']
        employee.country = request.data['country']
        employee.phone_number = request.data['phone_number']

        try:
            employee.save()
            serializer = EmployeeSerializer(employee, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:

            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handle PUT requests for a employee

        Returns:
            Response -- Empty body with 204 status code
        """

        if not request.auth.user.is_staff:
           return Response({}, status=status.HTTP_403_FORBIDDEN)

        employee = Employee.objects.get(pk=pk)
        employee.birth_date = request.data["birth_date"]
        employee.address = request.data['address']
        employee.city = request.data['city']
        employee.state = request.data['state']
        employee.postal_code = request.data['postal_code']
        employee.country = request.data['country']
        employee.phone_number = request.data['phone_number']
        employee.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single employee

        Returns:
            Response -- 200, 404, or 500 status code
        """
        if not request.auth.user.is_staff:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        try:
            employee = Employee.objects.get(pk=pk)
            employee.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Employee.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False, permission_classes=[IsAdminUser])
    def test(self, request):
        return Response('It worked')