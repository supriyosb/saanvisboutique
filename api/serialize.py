from rest_framework import serializers
from .models import Customer, CustomerPayment, CustomerProduct, CustomerTransaction, Vendor


class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['id', 'name', 'phone_no']


class CustomerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerProduct
        fields = ['id', 'transaction', 'prod_name', 'prod_quantity', 'total_price']


class CustomerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPayment
        fields = ['id', 'transaction', 'payment_amount', 'payment_date', 'payment_mode']


class CustomerPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerPayment
        fields = ['id', 'transaction', 'payment_amount', 'payment_date', 'payment_mode']


class CustomerTransactionSerializer(serializers.ModelSerializer):
    product = CustomerProductSerializer(many = True, read_only=True)
    payment = CustomerPaymentSerializer(many = True, read_only=True)
    class Meta:
        model = CustomerTransaction
        fields = ['id', 'customer', 'desc', 'paid_amount', 'due_amount', 'date', 'product', 'payment']


class CustomerSerializer(serializers.ModelSerializer):
    transaction = CustomerTransactionSerializer(many=True, read_only=True)
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone_no', 'transaction']