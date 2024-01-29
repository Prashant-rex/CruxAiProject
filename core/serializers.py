from rest_framework import serializers
from .models import FoodTruck

class FoodTruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTruck
        fields = ('name', 'latitude', 'longitude')

    latitude = serializers.SerializerMethodField()
    longitude = serializers.SerializerMethodField()

    def get_latitude(self, instance):
        return instance.current_location.latitude
    
    def get_longitude(self, instance):
        return instance.current_location.longitude






