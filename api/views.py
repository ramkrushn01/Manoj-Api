from django.shortcuts import render
from rest_framework import viewsets
from .models import Product, MyProduct
from .serializers import ProductSerializer, MyProductSerializer
# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class MyProductViewSet(viewsets.ModelViewSet):
    queryset = MyProduct.objects.all()
    serializer_class = MyProductSerializer