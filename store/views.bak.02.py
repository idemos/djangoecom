#from django.db import connection
from django.http import HttpResponse
from django.db.models import Count,Sum,Min,Max,F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer,ProductCategorySerializer
from django.shortcuts import render,get_object_or_404


@api_view()
def category_list(request):
    category = Category.objects.all()
    serializer = CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        product=Product.objects.all()
        serializer=ProductSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            return Response("ok")
        else:
            return Response(serializer.errors, status.HTTP_404_NOT_FOUND)

@api_view()
def product_category_list(request):
    products=Product.objects.select_related('category').order_by('-inventory')
    serializer=ProductCategorySerializer(products, many=True)
    return Response(serializer.data)

@api_view()
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    serializer=ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def category_detail(request,id):
    category = get_object_or_404(Category,pk=id)
    serializer=CategorySerializer(category)
    return Response(serializer.data)

@api_view()
def product_category_detail(request,id):
    products=get_object_or_404(Product.objects.select_related('category'),pk=id)
    serializer=ProductCategorySerializer(products)
    return Response(serializer.data)



# @api_view()
# def category_product_list(request):
#     products=Category.objects.select_related('products').order_by('-position')
#     serializer=CategoryProductSerializer(products, many=True)
#     return Response(serializer.data)