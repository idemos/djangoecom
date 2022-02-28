from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# per fare le ricerche
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from .models import Product,Category,OrderItem
from .serializers import CategorySerializer,ProductSerializer,ProductCategorySerializer
from django.shortcuts import get_object_or_404

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
    #queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get_queryset(self):
        queryset=Product.objects.all()
        category_id=self.request.query_params.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category=category_id)

        return queryset

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
