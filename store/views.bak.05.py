#from django.db import connection
from django.http import HttpResponse
from django.db.models import Count,Sum,Min,Max,F
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer,ProductCategorySerializer
from django.shortcuts import render,get_object_or_404

class CategoryList(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    def get_serializer_context(self):
        return {'request',self.request}

class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def delete(self,request,pk):
        category = get_object_or_404(Category,pk=pk)
        #orderitems=relation_name
        if category.products.count()>0:
            return Response({'ERROR':'non posso cancellar eun prodotto associato ad un ordine'}, status.HTTP_405_METHOD_NOT_ALLOWED)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProductList(ListCreateAPIView):
    queryset=Product.objects.select_related('category').order_by('-inventory')
    serializer_class=ProductSerializer

    def get_serializer_context(self):
        return {'request',self.request}

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def delete(self,request,pk):
        product = get_object_or_404(Product,pk=pk)
        #orderitems=relation_name
        if product.orderitems.count()>0:
            return Response({'ERROR':'non posso cancellar eun prodotto associato ad un ordine'}, status.HTTP_405_METHOD_NOT_ALLOWED)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    
@api_view()
def product_category_list(request):
    products=Product.objects.select_related('category').order_by('-inventory')
    serializer=ProductCategorySerializer(products, many=True)
    return Response(serializer.data)


@api_view()
def product_category_detail(request,id):
    products=get_object_or_404(Product.objects.select_related('category'),pk=id)
    serializer=ProductCategorySerializer(products)
    return Response(serializer.data)
