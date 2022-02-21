from django.urls import path
from . import views

urlpatterns = [
	path('category/<int:id>', views.CategoryDetail.as_view()),
	path('category', views.CategoryList.as_view()),
	path('product/<int:id>', views.product_detail),
	path('product', views.product_list),
	#path('product', views.ProductList.as_view()),
	#path('product/<int:id>', views.ProductDetail.as_view()),
	path('product_category/<int:id>', views.product_category_detail),
	path('product_category', views.product_category_list),
	#path('category_product', views.category_product_list),
]
