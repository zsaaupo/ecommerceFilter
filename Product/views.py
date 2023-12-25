from django.shortcuts import render
from .models import Product
from Category.models import Categories, Brand, Seller, Warranty, ProductType
from .serializers import ProductSerializer

from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.utils import json

class ProductList(ListAPIView):
    
    permission_classes=[]
    
    def get(self, request):
        
        product_list = Product.objects.all().order_by("name")
        product_list = ProductSerializer(product_list, many=True).data
        
        return Response(product_list)
    
    
class FilterProduct(CreateAPIView):
    
    permission_classes = []
    
    def post(self, request):
        result = {}
        
        try:
            data = json.loads(request.body)
            
            categories = data.get("category", [])
            brands = data.get("brand", [])
            sellers = data.get("seller", [])
            warranties = data.get("warranty", [])
            product_types = data.get("productType", [])
            
            filtered_product = {}

            if categories:
                filtered_product['category__in'] = categories
            if brands:
                filtered_product['brand__in'] = brands
            if sellers:
                filtered_product['seller__in'] = sellers
            if warranties:
                filtered_product['warranty__in'] = warranties
            if product_types:
                filtered_product['product_type__in'] = product_types
            if not filtered_product:
                products = Product.objects.all()
            else:
                products = Product.objects.filter(**filtered_product)
                
            serializer = ProductSerializer(products, many=True).data
            
            return Response(serializer)
        except Exception as ex:
            result = {}
            result['message'] = str(ex)
            return Response(result)