from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets,status
from rest_framework import response
from .models import Combinedata
from .serializers import CombinedDataSerializer,RequestPayloadSerializer
import requests

# Create your views here.   

class CombinedDataViewSet(viewsets.ViewSet):
    def list(self, request):
        combined_data = Combinedata.objects.all()
        serializer = CombinedDataSerializer(combined_data, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = RequestPayloadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        customer_id = serializer.validated_data['customer_id']

        pack1_data = requests.get('https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack1').json()
        pack2_data = requests.get('https://6466e9a7ba7110b663ab51f2.mockapi.io/api/v1/pack2').json()


        combined_data = {
            "customer_id": customer_id,
            "pack1": [f"{item['ingredient']} {item['quantity']}{item['unit']}" for item in pack1_data],
            "pack2": [f"{item['ingredient']} {item['quantity']}{item['unit']}" for item in pack2_data]
        }

        combined_serializer = CombinedDataSerializer(data=combined_data)
        combined_serializer.is_valid(raise_exception=True)
        combined_serializer.save()

        return response(combined_data, status=status.HTTP_201_CREATED)
    
    
