from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.CustomerViewSet)

urlpatterns = [
    path("view_customers/", views.CustomerView.as_view(), name='views.view_customers'), #Viewing customers template
    path('add_customer/', views.add_customer, name ='views.add_customer'),# Add customers REST DRF
    path('add_customers/', views.add_customer_template, name ='views.add_customers'),  #Add customers template
    path('',include(router.urls))
]


