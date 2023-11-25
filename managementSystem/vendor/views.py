from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.response import Response
import datetime
import os


class VendorViewset(viewsets.ModelViewSet):

    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    pagination_class = PageNumberPagination
    

class PurchaseOrderViewset(viewsets.ModelViewSet):

    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    pagination_class = PageNumberPagination
