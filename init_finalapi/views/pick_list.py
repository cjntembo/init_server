"""View module for handling requests about pick_lists"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.decorators import action
from init_finalapi.models import PickList, Employee, Customer
from init_finalapi.serializers.pick_list_serializer import PickListSerializer

class PickListView(ViewSet):
    """Init PickList"""
    @permission_classes([AllowAny])
    def retrieve(self, request, pk=None):
        """Handle Get Requests for single PickList
        Returns --JSON serialized pick_list
        """
        try:
            pick_list = PickList.objects.get(pk=pk)
            serializer = PickListSerializer(pick_list, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    @permission_classes([AllowAny])
    def list(self, request):
        """Gets all BinLocations"""

        pick_list = PickList.objects.all()

        serializer = PickListSerializer(pick_list, many=True, context={'request': request})
        return Response(serializer.data)

    # @permission_classes([IsAdminUser])
    @permission_classes([AllowAny])
    def create(self, request):
        """Handle Post Operations
        Returns:
        Response -- JSON serialized a pick_list instance
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        pick_list = PickList()
        customer = Customer.objects.get(pk=request.data['customerId'])
        pick_list.customer = customer
        picked_by = Employee.objects.get(pk=request.data['employeeId'])
        pick_list.picked_by = picked_by
        pick_list.pick_list_date = request.data['pick_list_date']

        try:
            pick_list.save()
            serializer = PickListSerializer(pick_list, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:

            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    @permission_classes([AllowAny])
    def update(self, request, pk=None):
        """Handle PUT requests for a pick_list

        Returns:
            Response -- Empty body with 204 status code
        """

        # if not request.auth.user.is_staff:
        #    return Response({}, status=status.HTTP_403_FORBIDDEN)

        pick_list = PickList(pk=pk)
        customer = Customer.objects.get(pk=request.data['customerId'])
        pick_list.customer = customer
        picked_by = Employee.objects.get(pk=request.data['employeeId'])
        pick_list.picked_by = picked_by
        pick_list.pick_list_date = request.data['pick_list_date']
        pick_list.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @permission_classes([AllowAny])
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single pick_list

        Returns:
            Response -- 200, 404, or 500 status code
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        try:
            pick_list = PickList.objects.get(pk=pk)
            pick_list.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PickList.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False, permission_classes=[IsAdminUser])
    def test(self, request):
        return Response('It worked')