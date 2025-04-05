from django.contrib import admin
from .models import Profile, Product, Suplier, Registry, Deposit, Price, Order, OrderItem

# Register your models here.
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Suplier)
admin.site.register(Registry)
admin.site.register(Deposit)
admin.site.register(Price)
admin.site.register(Order)
admin.site.register(OrderItem)