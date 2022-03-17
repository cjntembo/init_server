"""View module for handling requests about inventories"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.decorators import action
from init_finalapi.models import Inventory, Employee
from init_finalapi.serializers.inventory_serializer import InventorySerializer

class InventoryView(ViewSet):
    """Init Inventory"""
    @permission_classes([AllowAny])
    def retrieve(self, request, pk=None):
        """Handle Get Requests for single Inventory
        Returns --JSON serialized inventory
        """
        try:
            inventory = Inventory.objects.get(pk=pk)
            serializer = InventorySerializer(inventory, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    @permission_classes([AllowAny])
    def list(self, request):
        """Gets all Inventories"""
        inventory = Inventory.objects.all()
        serializer = InventorySerializer(inventory, many=True, context={'request': request})
        return Response(serializer.data)

    # @permission_classes([IsAdminUser])
    @permission_classes([AllowAny])
    def create(self, request):
        """Handle Post Operations
        Returns:
        Response -- JSON serialized an inventory instance
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        inventory = Inventory()
        inventory.description = request.data["description"]
        inventory.unit_price = request.data['unit_price']
        inventory.qty_available = request.data['qty_available']
        inventory.bin_location = request.data['bin_location']
        created_by = Employee.objects.get(pk=['employeeId'])
        inventory.created_by = created_by

        try:
            inventory.save()
            serializer = InventorySerializer(inventory, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:

            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([AllowAny])
    def update(self, request, pk=None):
        """Handle PUT requests for a inventory

        Returns:
            Response -- Empty body with 204 status code
        """

        # if not request.auth.user.is_staff:
        #    return Response({}, status=status.HTTP_403_FORBIDDEN)

        inventory = Inventory.objects.get(pk=pk)
        inventory.description = request.data["description"]
        inventory.unit_price = request.data['unit_price']
        inventory.qty_available = request.data['qty_available']
        inventory.bin_location = request.data['bin_location']
        created_by = Employee.objects.get(pk=['employeeId'])
        inventory.created_by = created_by
        inventory.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @permission_classes([AllowAny])
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single inventory

        Returns:
            Response -- 200, 404, or 500 status code
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        try:
            inventory = Inventory.objects.get(pk=pk)
            inventory.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Inventory.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False, permission_classes=[IsAdminUser])
    def test(self, request):
        return Response('It worked')