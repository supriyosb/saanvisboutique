from django.contrib import admin
from .models import Customer, CustomerPayment, CustomerProduct, CustomerTransaction, Vendor    

# Register your models here.
admin.site.register(Customer)
admin.site.register(Vendor)
admin.site.register(CustomerTransaction)
admin.site.register(CustomerProduct)
admin.site.register(CustomerPayment)

