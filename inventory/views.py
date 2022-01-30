from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import InventorySerializer
from .models import Inventory
from django.views import generic
from django.shortcuts import render




class InventoryView(generic.ListView):
    ''' View for Inventory DRF Rest'''

    model = Inventory
    template_name = 'inventory/index.html'

    def get_queryset(self):
        return Inventory.objects.all()

class InventoryViewSet(viewsets.ModelViewSet):
    ''' View for inventory Template '''

    queryset = Inventory.objects.all().order_by('vehicle_type')
    serializer_class = InventorySerializer




  
