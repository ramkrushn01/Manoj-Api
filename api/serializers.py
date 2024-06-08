from rest_framework import serializers
from .models import Product, MyProduct, Images

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class MyProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyProduct
        fields = "__all__"
