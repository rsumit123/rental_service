from rest_framework import serializers
from .models import Customers

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    '''Customer model serializer '''
    
    class Meta:
        model = Customers
        fields = ('name','email','phone')