from rest_framework import serializers
from .models import Customer, CustomerTransaction, Vendor

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone_no']


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'phone_no']


class CustomerTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerTransaction
        fields = ['id', 'customer', 'desc', 'total_amount', 'paid_amount', 'due_amount', 'date']