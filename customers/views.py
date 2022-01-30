from django.shortcuts import render, redirect
from rest_framework import viewsets
from django.http import JsonResponse
from .serializers import CustomerSerializer
from .models import Customers
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomerForm
from django.views import generic



class CustomerViewSet(viewsets.ModelViewSet):
    ''' View all customers DRF Rest '''

    queryset = Customers.objects.all().order_by('name')
    serializer_class = CustomerSerializer



class CustomerView(generic.ListView):
    ''' View all Customers template '''

    model = Customers
    template_name = 'customers/index.html'

    def get_queryset(self):
        return Customers.objects.all()

@csrf_exempt
def add_customer(request):
    ''' Add new customers for DRF '''

    if request.method == "POST":

        try:

            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']

            user = Customers(name=name , email = email, phone=phone)

            user.save()

            return JsonResponse({"success":True,"error":"False","message":"Customer added successfully"})

        except Exception as e:

            return JsonResponse({"success":False,"error":True,"message":str(e)})

    
    else:
        return JsonResponse({"success":False,"error":True,"message":"Incorrect Request Format"})

def add_customer_template(request):
    ''' Add a new customer template '''

    context ={}
  
    # create object of form
    form = CustomerForm(request.POST or None)
      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
        return redirect("/customers/view_customers") #redirect to avoid multiple submit
  
    context['form']= form
    return render(request, "customers/add_customers.html", context)
