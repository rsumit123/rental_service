from django import forms
from .models import Customers
  
class CustomerForm(forms.ModelForm):
    ''' Simple Customer modelForm '''
    
    class Meta:
        model = Customers
        fields = "__all__"