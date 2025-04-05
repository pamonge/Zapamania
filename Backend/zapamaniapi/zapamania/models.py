from django.db import models
from django.contrib.auth.models import User

# Create your models here
class Profile(models.Model):
    user_type = [
        ('p', 'provider'),
        ('c', 'client'),
        ('a', 'admin'),
        ('d', 'deposit'),
        ('s', 'sales'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='profile_pic/', blank=True, null=True)
    phone = models.IntegerField(verbose_name='telefono', blank=True, null=True)
    address = models.CharField(max_length=100, verbose_name='direccion')
    userType = models.CharField(max_length=1, choices=user_type, verbose_name='tipo de usuario')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'perfil'

#Clase referente a los productos
class Product(models.Model):
    productName = models.CharField(max_length=50, verbose_name='nombre')
    productSize = models.IntegerField(verbose_name='talle')
    productColor = models.CharField(max_length=50, verbose_name='color')

    def __str__(self):
        return self.productName
    
    class Meta:
        verbose_name = 'producto'

#Clase que crea proveedores
class Suplier(models.Model):
    SUP_LOCATION = [
        ('bas', 'buenos aires'),
        ('cte', 'corrientes'),
        ('fsa', 'formosa'),
        ('mza', 'mendoza'),
        ('pam', 'la pampa'),
        ('sfe', 'santa fe'),
        ('slu', 'san luis'),
        ('cru', 'santa cruz'),
        ('tuc', 'tucuman'),
        ('cat', 'catamarca'),
        ('juj', 'jujuy'),
        ('sal', 'salta'),
        ('cap', 'capital federal'),
        ('sju', 'san juan'),
        ('sgo', 'santiago del estero'),
        ('chu', 'chubut'),
        ('eri', 'entre rios'),
        ('rne', 'rio negro'),
        ('rio', 'la rioja'),
        ('neu', 'neuquen'),
        ('mis', 'misiones'),
        ('cba', 'cordoba'),
        ('fgo', 'tierra del fuego'),
        ('cha', 'chaco'),
    ]

    suplierName = models.CharField(max_length=50, verbose_name='proveedor')
    suplierPhone = models.IntegerField(verbose_name='telefono')
    suplierAddress = models.CharField(max_length=50, verbose_name='direccion')
    suplierLocation = models.CharField(max_length=3, verbose_name='provincia')

    def __str__(self):
        return self.suplierName

    class Meta:
        verbose_name = 'proveedor'

#Registra nuevos productos
class Registry(models.Model):

    STATUS_CHOICES = [
        ('a', 'alta'),
        ('b', 'baja'),
    ]

    CAUSE_CHOICES = [
        ('c', 'compra'),
        ('v', 'venta'),
        ('d', 'devolucion'),
        ('e', 'error'),
        ('o', 'otro'),
    ]

    registryProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='inventario')
    quantity = models.IntegerField(verbose_name='cantidad')
    order = models.CharField(max_length=50, verbose_name='orden')
    registryOp = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name='operacion')
    cause = models.CharField(max_length=1,choices=CAUSE_CHOICES , verbose_name='causa')
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE, verbose_name='proveedor')

    def __str__(self):
        return self.registryProduct.productName

    class Meta:
        verbose_name = 'registro'

class Deposit(models.Model):
    depProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='deposito')
    depQuantity = models.IntegerField(verbose_name='cantidad')
    lastUpdate = models.DateTimeField(auto_now=True, verbose_name='ultima actualizacion')

    def __str__(self):
        return self.depProduct.productName

    class Meta:
        verbose_name = 'deposito'

class Price(models.Model):
    PRICE_VAR = [
        ('b', 'caja'),
        ('p', 'papel'),
        ('s', 'envio'),
    ]
    
    priceCoef = models.DecimalField(max_digits=3, decimal_places=2, verbose_name='coeficiente')
    priceSuplier = models.ForeignKey(Suplier, on_delete=models.CASCADE, verbose_name='proveedor')
    priceProd = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='precio Producto')

    def __str__(self):
        return priceSuplier.suplierName

    class Meta:
        verbose_name = 'precio'

class Order(models.Model):
    statusChoices = [
        ('p', 'pending'),
        ('c', 'accomplish'),
        ('r', 'rejected')
    ]
    client = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='cliente')
    suplier = models.ForeignKey(Suplier, on_delete=models.CASCADE, verbose_name='provedor')
    status = models.CharField(max_length=1, choices=statusChoices, verbose_name='estado de orden')
    created = models.DateTimeField(auto_now_add=True, verbose_name='fecha de creación')

    def __str__(self):
        return Order.id

    class Meta:
        verbose_name = 'orden'

class OrderItem(models.Model):
    orderNum = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='numero de orden')
    productItem = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Items')
    productQuantity = models.IntegerField(verbose_name='cantidad')

    def __str__(self):
        return f'orden {self.orderNum}, producto {self.productItem}, cantidad {self.productQuantity}'

    class Meta:
        verbose_name = 'item de la orden'
