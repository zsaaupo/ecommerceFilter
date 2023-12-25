from django.shortcuts import render
from .models import Product
from Category.models import Categories, Brand, Seller, Warranty, ProductType
from .serializers import ProductSerializer

from rest_framework.generics import ListAPIView
from rest_framework.response import Response

class ProductList(ListAPIView):
    
    permission_classes=[]
    
    def get(self, request):
        
        product_list = Product.objects.all()
        product_list = ProductSerializer(product_list, many=True).data
        
        return Response(product_list)