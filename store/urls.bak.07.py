from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from pprint import pprint

router = DefaultRouter()
router.register('carts', views.CartViewSet)
#router.register('product', views.ProductViewSet, basename='product')
router.register('category', views.CategoryViewSet)

#urlpatterns = router.urls
#oppure

urlpatterns = [
	path('', include(router.urls)),
	#path('product_category/<int:id>', views.product_category_detail),
	#path('product_category/?$', views.product_category_list),
]
