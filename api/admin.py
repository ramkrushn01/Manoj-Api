from django.contrib import admin
from .models import Product, MyProduct, Images
# Register your models here.

admin.site.register(Product)
admin.site.register(MyProduct)
admin.site.register(Images)