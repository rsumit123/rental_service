from django.db import models

class Customers(models.Model):
    '''
     The customer model
    '''
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254,unique=True)
    phone = models.CharField(max_length=15, unique=True)


    def __str__(self):
        
        return f"{self.email}"

    class Meta:
        '''
        For changing the table name and plural names
        '''
        db_table = "Customers"
        verbose_name_plural = "customers"
