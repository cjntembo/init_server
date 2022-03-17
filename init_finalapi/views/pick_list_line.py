"""View module for handling requests about pick_list_lines"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.decorators import action
from init_finalapi.models import PickListLine, PickList, Inventory
from init_finalapi.serializers.pick_list_line_serializer import PickListLineSerializer

class PickListLineView(ViewSet):
    """Init PickListLine"""
    @permission_classes([AllowAny])
    def retrieve(self, request, pk=None):
        """Handle Get Requests for single PickListLine
        Returns --JSON serialized pick_list_line
        """
        try:
            pick_list_line = PickListLine.objects.get(pk=pk)
            serializer = PickListLineSerializer(pick_list_line, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)
    @permission_classes([AllowAny])
    def list(self, request):
        """Gets all BinLocations"""
        pick_list_line = PickListLine.objects.all()
        serializer = PickListLineSerializer(pick_list_line, many=True, context={'request': request})
        return Response(serializer.data)

    # @permission_classes([IsAdminUser])
    @permission_classes([AllowAny])
    def create(self, request):
        """Handle Post Operations
        Returns:
        Response -- JSON serialized a pick_list_line instance
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        pick_list_line = PickListLine()
        pick_list = PickList.objects.get(pk=request.data['pick_listId'])
        pick_list_line.pick_list = pick_list
        inventory = Inventory.objects.get(pk=request.data['inventoryId'])
        pick_list_line.inventory = inventory
        pick_list_line.qty_requested = request.data['qty_requested']

        try:
            pick_list_line.save()
            serializer = PickListLineSerializer(pick_list_line, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:

            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)
    
    @permission_classes([AllowAny])
    def update(self, request, pk=None):
        """Handle PUT requests for a pick_list_line

        Returns:
            Response -- Empty body with 204 status code
        """

        # if not request.auth.user.is_staff:
        #    return Response({}, status=status.HTTP_403_FORBIDDEN)

        pick_list_line = PickListLine(pk=pk)
        pick_list = PickList.objects.get(pk=request.data['pick_listId'])
        pick_list_line.pick_list = pick_list
        inventory = Inventory.objects.get(pk=request.data['inventoryId'])
        pick_list_line.inventory = inventory
        pick_list_line.qty_requested = request.data['qty_requested']
        pick_list_line.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    @permission_classes([AllowAny])
    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single pick_list_line

        Returns:
            Response -- 200, 404, or 500 status code
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        try:
            pick_list_line = PickListLine.objects.get(pk=pk)
            pick_list_line.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except PickListLine.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False, permission_classes=[IsAdminUser])
    def test(self, request):
        return Response('It worked')