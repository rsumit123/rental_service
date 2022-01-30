from rest_framework import serializers
from .models import Inventory

class InventorySerializer(serializers.HyperlinkedModelSerializer):
    ''' Inventory serializer for Inventory model '''
    
    class Meta:
        model = Inventory
        fields = ('vehicle_type','available_quantity')