from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', views.BookingViewSet)

urlpatterns = [
    path("view_bookings/", views.BookingView.as_view(), name='views.view_bookings'), #Template View for viewing bookings
    path('add_booking/', views.add_booking, name ='views.add_booking'),  #DRF view for adding booking
    path('make_booking/', views.make_booking_template, name = 'views.make_booking'), #Template view for adding new booking
    path('',include(router.urls))
]


