from django import forms
from .models import Bookings
  
class BookingsForm(forms.ModelForm):
    ''' Bookings model form '''
    class Meta:
        model = Bookings
        fields = "__all__"