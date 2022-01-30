from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from rest_framework import viewsets

from django.views import generic
from django.shortcuts import render



def index(request):
    """View function for home page of site."""

    return render(request, 'home/home.html')


  
