from rest_framework import serializers
from .models import *
import re

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'username',
         'password', 'email','address', 'phone')
        # fields = '__all__' 
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_password(self, password):
        if len(password) < 8:
            raise serializers.ValidationError("The password must contain at least 8 characters")
        if not re.findall('\d', password):
            raise serializers.ValidationError("The password must contain at least 1 digit, 0-9.")
        if not re.findall('[A-Z]', password):
            raise serializers.ValidationError("The password must contain at least 1 uppercase letter, A-Z.")
        if not re.findall('[a-z]', password):
            raise serializers.ValidationError("The password must contain at least 1 lowercase letter, a-z.")
        if not re.findall('[!@#$%^&*()]', password):
            raise serializers.ValidationError("The password must contain at least 1 symbol: " + "!@#$%^&*()")
        return password

    def create(self, validated_data):

        if validated_data:

            user = User.objects.create(**validated_data)
            user.set_password(validated_data['password'])
            user.save()


            return user
        else:
            raise serializers.ValidationError


class VendorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vendor
        fields = '__all__'
        extra_kwargs = {'vendor_code': {'read_only': True,"required": False, "allow_null": True}}


class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        extra_kwargs = {'po_number': {'read_only': True}}


class HistoricalPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformance
        fields = '__all__'
