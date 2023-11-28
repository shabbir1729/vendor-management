from django.urls import path,include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

apiRouter = routers.DefaultRouter()

apiRouter.register(r'vendors', VendorViewset, basename='vendors')
apiRouter.register(r'purchase_orders', PurchaseOrderViewset, basename='purchase_orders')



urlpatterns = [
    path('api/', include(apiRouter.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]