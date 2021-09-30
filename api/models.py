from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)

class CustomerTransaction(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, related_name='transaction')
    desc = models.TextField()
    total_amount = models.DecimalField(max_digits=20, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=20, decimal_places=2)
    due_amount = models.DecimalField(max_digits=20, decimal_places=2)
    date = models.DateField(auto_now=False, auto_now_add=False)

class CustomerProduct(models.Model):
    transaction = models.ForeignKey(CustomerTransaction, on_delete=models.DO_NOTHING, related_name='product')
    prod_name = models.CharField(max_length=50)
    prod_quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=2)
