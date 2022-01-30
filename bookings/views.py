from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import BookingSerializer
from .models import Bookings
from customers.models import Customers
from inventory.models import Inventory
from .forms import BookingsForm
from django.views import generic
from inventory.models import Inventory
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


class BookingViewSet(viewsets.ModelViewSet):
    ''' DRF view for viewing all bookings '''
    queryset = Bookings.objects.all().order_by('customer')
    serializer_class = BookingSerializer



class BookingView(generic.ListView):

    ''' Template View for viewing all bookings '''

    model = Bookings
    template_name = 'bookings/index.html'

    def get_queryset(self):
        return Bookings.objects.all()

@csrf_exempt
def add_booking(request):

    '''Add booking view for DRF'''

    if request.method == "POST":

        customer_email = request.POST['email']
        vehicle_type = request.POST['vehicle_type']
        try:
            return_date = request.POST['return_date']
        except:
            return_date = ""

        try:
            user = Customers.objects.get(email = customer_email)

        except Customers.DoesNotExist:

            return JsonResponse({"error":"Customer does not exist"})

        try:
            vehicle = Inventory.objects.get(vehicle_type = vehicle_type)  #Decease inventory quantity by 1
            vehicle.available_quantity = vehicle.available_quantity - 1
            vehicle.save()

        except Exception as e:

            return JsonResponse({"error":str(e)})

        if return_date == "":

            ordr = Bookings(customer = user , vehicle_type = vehicle )
            ordr.save()
        
        else:

            ordr = Bookings(customer = user , vehicle_type = vehicle, return_date = return_date )
            ordr.save()


        return JsonResponse({"error":False, "success": True, "message": "Booking made successfully"})


    else:

        return JsonResponse({"error":True, "success": False, "message": "Incorrect Request Format"})


def make_booking_template(request):
    '''View for BookingForm '''
    context ={}
  
    # create object of form
    form = BookingsForm(request.POST or None)
      
    # check if form data is valid
    if form.is_valid():
        #Decrease the selected vehicle Inventory Type
        
        inventories = Inventory.objects.all()
        ind = form.data["vehicle_type"]
        vehicle_type = inventories[int(ind)-1].vehicle_type

        if inventories[int(ind)-1].available_quantity > 0:

            
            inventory_obj = Inventory.objects.get(vehicle_type = vehicle_type)
            inventory_obj.available_quantity = inventory_obj.available_quantity - 1
            inventory_obj.save()
            form.save()
            return redirect("/bookings/view_bookings")
        else:
            #If inventory less than 0 raise error
            messages.error(request, f"Inventory for the selected vehicle, {vehicle_type}, not available.. Please chose a different Vehicle ")

        
        
  
    context['form']= form
    return render(request, "bookings/make_booking.html", context)


    