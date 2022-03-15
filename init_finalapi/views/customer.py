"""View module for handling requests about customers"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from init_finalapi.models import Customer
from init_finalapi.serializers.customer_serializer import CustomerSerializer

class CustomerView(ViewSet):
    """Init Customers"""
    def retrieve(self, request, pk=None):
        """Handle Get Requests for single Customer
        Returns --JSON serialized customer
        """
        try:
            customer = Customer.objects.get(pk=pk)
            serializer = CustomerSerializer(customer, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Gets all Customers"""
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True, context={'request': request})
        return Response(serializer.data)

    # @permission_classes([IsAdminUser])
    def create(self, request):
        """Handle Post Operations
        Returns:
        Response -- JSON serialized an customer instance
        """
        if not request.auth.user.is_staff:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        customer = Customer()
        customer.email = request.data["email"]
        customer.company = request.data["company"]
        customer.first_name = request.data["first_name"]
        customer.last_name = request.data["last_name"]
        customer.address = request.data['address']
        customer.city = request.data['city']
        customer.state = request.data['state']
        customer.postal_code = request.data['postal_code']
        customer.country = request.data['country']
        customer.phone_number = request.data['phone_number']

        try:
            customer.save()
            serializer = CustomerSerializer(customer, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:

            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handle PUT requests for a category

        Returns:
            Response -- Empty body with 204 status code
        """

        if not request.auth.user.is_staff:
           return Response({}, status=status.HTTP_403_FORBIDDEN)

        customer = Customer.objects.get(pk=pk)
        customer.email = request.data["email"]
        customer.company = request.data["company"]
        customer.first_name = request.data["first_name"]
        customer.last_name = request.data["last_name"]
        customer.address = request.data['address']
        customer.city = request.data['city']
        customer.state = request.data['state']
        customer.postal_code = request.data['postal_code']
        customer.country = request.data['country']
        customer.phone_number = request.data['phone_number']
        customer.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single category

        Returns:
            Response -- 200, 404, or 500 status code
        """
        if not request.auth.user.is_staff:
            return Response({}, status=status.HTTP_403_FORBIDDEN)

        try:
            customer = Customer.objects.get(pk=pk)
            customer.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Customer.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False, permission_classes=[IsAdminUser])
    def test(self, request):
        return Response('It worked')