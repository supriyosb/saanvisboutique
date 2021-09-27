from api.serialize import CustomerSerializer, CustomerTransactionSerializer, VendorSerializer
from .models import Customer, CustomerTransaction, Vendor
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView

class CustomerAPI(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        data = Customer.objects.all()
        serializer= CustomerSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            last_data = Customer.objects.last()
            last_data_serializer = CustomerSerializer(last_data)
            return Response({'msg': 'Data Created', 'success': True, 'data': last_data_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None, pk=None):
        try:
            if pk is not None:
                customer = Customer.objects.get(id=pk)
                serializer = CustomerSerializer(customer, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': 'Data Updated', 'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'msg': 'Customer id not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, format=None, pk=None):
        try:
            if pk is not None:
                customer_data = Customer.objects.get(id=pk)
                serializer= CustomerSerializer(customer_data)
                customer_data.delete()
                return Response({'msg': 'Data Deleted', 'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'msg': 'Customer id not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)





class VendorAPI(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        data = Vendor.objects.all()
        serializer= VendorSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            last_data = Vendor.objects.last()
            last_data_serializer = VendorSerializer(last_data)
            return Response({'msg': 'Data Created', 'success': True, 'data': last_data_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None, pk=None):
        try:
            if pk is not None:
                vendor = Vendor.objects.get(id=pk)
                serializer = VendorSerializer(vendor, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': 'Data Updated', 'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'msg': 'Vendor id not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, format=None, pk=None):
        try:
            if pk is not None:
                vendor_data = Vendor.objects.get(id=pk)
                serializer= VendorSerializer(vendor_data)
                vendor_data.delete()
                return Response({'msg': 'Data Deleted', 'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'msg': 'Vendor id not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class CustomerTransactionAPI(APIView):

    #permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        data = CustomerTransaction.objects.all()
        serializer= CustomerTransactionSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CustomerTransactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            last_data = CustomerTransaction.objects.last()
            last_data_serializer = CustomerTransactionSerializer(last_data)
            return Response({'msg': 'Data Created', 'success': True, 'data': last_data_serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, format=None, pk=None):
        try:
            if pk is not None:
                customerTransaction = CustomerTransaction.objects.get(id=pk)
                serializer = CustomerTransactionSerializer(customerTransaction, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response({'msg': 'Data Updated', 'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response({'msg': 'Customer transaction id not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, format=None, pk=None):
        try:
            if pk is not None:
                customer_transaction_data = CustomerTransaction.objects.get(id=pk)
                serializer= CustomerTransactionSerializer(customer_transaction_data)
                customer_transaction_data.delete()
                return Response({'msg': 'Data Deleted', 'success': True, 'data': serializer.data}, status=status.HTTP_200_OK)
        except Exception:
            return Response({'msg': 'Customer transaction id not found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
