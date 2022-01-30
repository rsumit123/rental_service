from django.db import models
from customers.models import Customers
from inventory.models import Inventory
class Bookings(models.Model):

    '''
     Bookings model
    '''
    customer = models.ForeignKey(Customers, on_delete=models.CASCADE )
    vehicle_type = models.ForeignKey(Inventory, on_delete=models.CASCADE )
    rental_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null = True, blank = True)
    

    def __str__(self):
        ''' Display name '''
        
        return f"{self.customer.name} | {self.vehicle_type.vehicle_type}"

    class Meta:
        '''
        For changing the table name and plural names
        '''
        db_table = "Bookings"
        verbose_name_plural = "bookings"
