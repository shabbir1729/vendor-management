from .models import Vendor,PurchaseOrder, HistoricalPerformance
from .serializer import UserSerializer,VendorSerializer,PurchaseOrderSerializer,HistoricalPerformanceSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
import datetime
from django.utils import timezone

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):

    queryset                = User.objects.all()
    serializer_class        = UserSerializer
    authentication_classes  = (JWTAuthentication,)


class VendorViewset(viewsets.ModelViewSet):

    queryset            = Vendor.objects.all()
    serializer_class    = VendorSerializer
    pagination_class    = PageNumberPagination
    permission_classes  = (IsAuthenticated,)

    
class PurchaseOrderViewset(viewsets.ModelViewSet):

    queryset            = PurchaseOrder.objects.all()
    serializer_class    = PurchaseOrderSerializer
    pagination_class    = PageNumberPagination
    permission_classes  = (IsAuthenticated,)


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_vendor_performace(request,po_id):

    performace_obj = Vendor.objects.get(id=po_id)
    performace_data = VendorSerializer(performace_obj)
    return Response (performace_data.data)


@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def acknowledge_po(request,po_id):

    po_object = PurchaseOrder.objects.get(id=po_id)
    po_object.acknowledgement_date = str(datetime.datetime.now())
    po_object.status = 'completed'
    po_object.save()
    serializer = PurchaseOrderSerializer(data=po_object,partial=True)
    
    if serializer.is_valid():
        serializer.save()

        return Response({"Message":"Success"})
    else:
        raise serializer.errors
    






