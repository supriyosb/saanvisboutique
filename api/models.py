from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)

class Vendor(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15)
