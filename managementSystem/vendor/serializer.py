from rest_framework import serializers
from .models import *

class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {'vendor_code': {'read_only': True}}


class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_kwargs = {'po_number': {'read_only': True}}


class HistoricalPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
