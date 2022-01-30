from rest_framework import serializers
from .models import Bookings

class BookingSerializer(serializers.HyperlinkedModelSerializer):
    ''' Serializer for booking model '''
    class Meta:
        model = Bookings
        fields = ('customer','vehicle_type','rental_date', "return_date")