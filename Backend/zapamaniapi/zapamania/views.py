from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from .models import Profile, Product, Suplier, Registry, Deposit, Price, Order, OrderItem
from .serializers import UserSerializer, ProfileSerializer, ProductSerializer, SuplierSerializer, RegistrySerializer, DepositSerializer, PriceSerializer, OrderSerializer, OrderItemSerializer

# Create your views here.
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SuplierViewSet(viewsets.ModelViewSet):
    queryset = Suplier.objects.all()
    serializer_class = SuplierSerializer

class RegistryViewSet(viewsets.ModelViewSet):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer

class DepositViewSet(viewsets.ModelViewSet):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer