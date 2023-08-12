from rest_framework import serializers
from .models import Combinedata


class CombinedDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Combinedata
        fields = ('id','customer_id','pack1','pack2' )

class RequestPayloadSerializer(serializers.Serializer):
    customer_id = serializers.IntegerField()
