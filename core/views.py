from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponseBadRequest

from .models import FoodTruck, Coordinates
from .serializers import FoodTruckSerializer
from .utils import calculate_distance

class FoodTruckView(APIView):

    def get(self, request):
        longitude = self.request.query_params.get('long')
        latitude = self.request.query_params.get('lat')
        distance = self.request.query_params.get('distance')

        if not latitude or not longitude:
            if float(latitude) is None or float(Longitude) is None:
                return HttpResponseBadRequest('Latitude and Longitude are required')
        
        if not distance:
            if float(distance) is None:
                distance = 5
        
        co_ords_queryset = Coordinates.objects.all()

        co_ordinates_id = []

        for q in co_ords_queryset:
            dist = calculate_distance(latitude, longitude, q.latitude, q.longitude)
            if dist <= float(distance):
                co_ordinates_id.append(q.id)
        
        queryset = FoodTruck.objects.filter(status='APPROVED', current_location_id__in=co_ordinates_id)

        serializer = FoodTruckSerializer(queryset, many=True)
        data = serializer.data

        return Response(data)


    
