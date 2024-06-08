from rest_framework import routers
from .views import ProductViewSet,MyProductViewSet
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'products',ProductViewSet)
router.register(r'myproducts', MyProductViewSet)

urlpatterns = [
    path('',include(router.urls)),
]