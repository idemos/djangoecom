#from django.db import connection
from django.http import HttpResponse
from django.db.models import Count,Sum,Min,Max,F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Category
from .serializers import ProductSerializer,CategorySerializer,ProductCategorySerializer
from django.shortcuts import render,get_object_or_404

@api_view()
def product_category_list(request):
    # products=Product.objects.all().order_by('-inventory')
    products=Product.objects.select_related('category').order_by('-inventory')
    serializer=ProductCategorySerializer(products,many=True)
    return Response(serializer.data)

@api_view()
def product_list(request):
    product=Product.objects.all()
    serializer=ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def product_detail(request,id):
    #product = get_object_or_404(Product,pk=id)
    product=Product.objects.select_related('category').get(pk=id); #.order_by('-inventory')
    serializer=ProductSerializer(product)
    return Response(serializer.data)

@api_view()
def category_list(request):
    category=Category.objects.all()
    serializer=CategorySerializer(category)
    return Response(serializer.data)


def annotate(request):
    products = Product.objects.annotate(new_id=F('id')+1)
    return render(request, 'store/annotate.html', {'products':products})

def aggregation(request):
    products = Product.objects.aggregate(Count('id'))
    return render(request, 'store/aggregation.html', {'products':products})

def connection(request):
    with connection.cursor() as cursor:
        queryset = cursor.execute('select * from store_product')
        return render(request, 'store/connection.html', {'products': list(queryset)})


# def listcustom(request):
#     queryset = Product.objects.raw('SELECT * FROM store_product')
#     return render(request, 'store/listcustom.html', {'products': list(queryset)})

def contactus(request):
    return render(request, 'store/contactus.html')

# Create your views here.
def list(request):
    # DAMMI I prim 2 
    # products = Product.objects.all().order_by('-inventory')[:2]
    # DAMMI dal 2 al 3
    # products = Product.objects.all().order_by('-inventory')[2:3]
    # selezionare specifici campi
    # products = Product.objects.values_list('category__name', 'image','name','description','unit_price')
    # products = Product.objects.values('category__name', 'image','name','description','unit_price')
    # products = Product.objects.select_related('category').all()
    products = Product.objects.aggregate(Count('id')).all()
    return render(request, 'store/list.html', {'products':products})


