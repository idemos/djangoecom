from django.urls import path,include
from . import views
from rest_framework_nested import routers
from pprint import pprint


router = routers.DefaultRouter()
router.register('carts', views.CartViewSet)
router.register('product', views.ProductViewSet, basename='product')
router.register('category', views.CategoryViewSet)

#pprint(router.urls)
products_router = routers.NestedDefaultRouter(router, 'product', lookup='product')
products_router.register('review',views.ReviewViewSet, basename='product-review')

urlpatterns = router.urls + products_router.urls

