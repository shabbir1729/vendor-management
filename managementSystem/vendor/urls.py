from django.urls import path,include
from .views import *
from rest_framework import routers

apiRouter = routers.DefaultRouter()

apiRouter.register(r'vendors', VendorViewset, basename='vendors')
apiRouter.register(r'purchase_orders', PurchaseOrderViewset, basename='purchase_orders')



urlpatterns = [
    path('api/', include(apiRouter.urls)),

]