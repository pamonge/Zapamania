from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserCreateView, 
    ProfileViewSet, 
    ProductViewSet, 
    SuplierViewSet, 
    RegistryViewSet, 
    DepositViewSet, 
    PriceViewSet,
    OrderViewSet,
    OrderItemViewSet,
)

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)
router.register(r'product', ProductViewSet)
router.register(r'registry', RegistryViewSet)
router.register(r'deposit', DepositViewSet)
router.register(r'price', PriceViewSet)
router.register(r'order', OrderViewSet)
router.register(r'order_item', OrderItemViewSet)

urlpatterns = [
    path('user/', UserCreateView.as_view(), name='userView'),
    path('', include(router.urls)), #rutas creadas con el router
]