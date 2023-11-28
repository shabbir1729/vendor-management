from .models import Vendor,PurchaseOrder
from .serializer import UserSerializer,VendorSerializer,PurchaseOrderSerializer
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model

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

