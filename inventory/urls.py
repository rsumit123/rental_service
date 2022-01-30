from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.InventoryViewSet)

urlpatterns = [
    
    path("view_inventory/", views.InventoryView.as_view(), name='views.view_inventory'), #Viewing inventory Template

path('',include(router.urls))
]


