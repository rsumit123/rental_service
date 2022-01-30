from django.db import models

# Create your models here


class Inventory(models.Model):
    '''
     The inventory model
    '''
    vehicle_type = models.CharField(max_length=50)
    available_quantity = models.IntegerField(default=1)


    def __str__(self):
        return f"{self.vehicle_type}"

    class Meta:
        '''
        For changing the table name and plural names
        '''
        db_table = "Inventory"
        verbose_name_plural = "inventories"
