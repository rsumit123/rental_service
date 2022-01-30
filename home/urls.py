from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('',views.index, name='index' ), #The home page of the site
    

path('',include(router.urls))
]
