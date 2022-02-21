#from django.db import connection
from django.http import HttpResponse
from django.db.models import Count,Sum,Min,Max,F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product,Category
from .serializers import CategorySerializer,ProductSerializer,ProductCategorySerializer
from django.shortcuts import render,get_object_or_404


@api_view(['GET','POST'])
def category_list(request):
    if request.method == 'GET':
        category = Category.objects.annotate(products_count=Count('products')).all()
        #category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=CategorySerializer(data=request.data)
        # controlla la validazione sul model
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# X visualizzare o creare un nuovo prodotto
@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        product=Product.objects.all()
        serializer=ProductSerializer(product, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer=ProductSerializer(data=request.data)
        # controlla la validazione sul model
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# X visualizzare o modificare un prodotto esistente
@api_view(['GET','PUT','DELETE'])
def product_detail(request,id):
    product = get_object_or_404(Product,pk=id)
    if request.method == 'GET':
        serializer=ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer=ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        #if product.orderitem_set.count()>0:
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