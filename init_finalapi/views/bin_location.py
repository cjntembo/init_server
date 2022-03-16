"""View module for handling requests about bin_locations"""
from django.forms import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from init_finalapi.models import BinLocation
from init_finalapi.serializers.bin_location_serializer import BinLocationSerializer

class BinLocationView(ViewSet):
    """Init BinLocation"""
    def retrieve(self, request, pk=None):
        """Handle Get Requests for single BinLocation
        Returns --JSON serialized bin_location
        """
        try:
            bin_location = BinLocation.objects.get(pk=pk)
            serializer = BinLocationSerializer(bin_location, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Gets all BinLocations"""
        bin_location = BinLocation.objects.all()
        serializer = BinLocationSerializer(bin_location, many=True, context={'request': request})
        return Response(serializer.data)

    # @permission_classes([IsAdminUser])
    def create(self, request):
        """Handle Post Operations
        Returns:
        Response -- JSON serialized a bin_location instance
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        bin_location = BinLocation()
        bin_location.bin_location_name = request.data["bin_location_name"]
        bin_location.binned_by = request.data['binned_by']

        try:
            bin_location.save()
            serializer = BinLocationSerializer(bin_location, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:

            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """Handle PUT requests for a bin_location

        Returns:
            Response -- Empty body with 204 status code
        """

        # if not request.auth.user.is_staff:
        #    return Response({}, status=status.HTTP_403_FORBIDDEN)

        bin_location = BinLocation.objects.get(pk=pk)
        bin_location.bin_location_name = request.data["bin_location_name"]
        bin_location.binned_by = request.data['binned_by']
        bin_location.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single bin_location

        Returns:
            Response -- 200, 404, or 500 status code
        """
        # if not request.auth.user.is_staff:
        #     return Response({}, status=status.HTTP_403_FORBIDDEN)

        try:
            bin_location = BinLocation.objects.get(pk=pk)
            bin_location.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except BinLocation.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=["get"], detail=False, permission_classes=[IsAdminUser])
    def test(self, request):
        return Response('It worked')