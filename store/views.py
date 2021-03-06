from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# per fare le ricerche
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.pagination import PageNumberPagination

from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin

from .filters import ProductFilter
from .models import CartItem, Product,Category,OrderItem,Cart,Review
from .serializers import CategorySerializer,ProductSerializer,ProductCategorySerializer,CartSerializer,ReviewSerializer
from django.shortcuts import get_object_or_404
from pprint import pprint


class ReviewViewSet(ModelViewSet):
    #queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        pprint(self.kwargs['product_pk'])
        return {'product_id': self.kwargs['product_pk']}


# class CartItemViewSet(ModelViewSet):

#     def get_queryset(self):
#         return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])

# la cart non puo essere modificata e non puo essere 
# fatta la get di tutte le cart esistenti 
# quindi creiamo un modeviewset custom

class CartViewSet(RetrieveModelMixin,CreateModelMixin,DestroyModelMixin,GenericViewSet):
#class CartViewSet(ModelViewSet):
    queryset=Cart.objects.prefetch_related('cartitems__product').all()
    #pprint(queryset)
    serializer_class=CartSerializer

class CategoryViewSet(ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

    def get_serializer_context(self):
        return {'request',self.request}

    def destroy(self, request, *args, **kwargs):
        if Product.object.filter(id=kwargs['pk']).count()>0:
            return Response({'ERROR':'non posso cancellar eun prodotto associato ad un ordine'}, status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

# con questa sintassi possiamo solo leggere
# e non fare operazione di scrittura
# class ProductViewSet(ReadOnlyModelViewSet):

class ProductViewSet(ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    #filterset_fields = ['category_id']
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination
    search_fields = ['name','description', 'category__name']
    ordering_fields = ['unit_price']

    def get_serializer_context(self):
        return {'request',self.request}
    # sovrascrive il modelview per quanto riguarda la cancellazione
    # cosi possiamo fare i dovuti controlli
    def destroy(self, request, *args, **kwargs):
        if OrderItem.object.filter(product_id=kwargs['pk']).count()>0:
            return Response({'ERROR':'non posso cancellar eun prodotto associato ad un ordine'}, status.HTTP_405_METHOD_NOT_ALLOWED)
        return super().destroy(request, *args, **kwargs)

    
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
