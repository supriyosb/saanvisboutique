from api.serialize import CustomerSerializer
from .models import Customer
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
