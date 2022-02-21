from django.urls import path
from . import views

urlpatterns = [
	path('category/<int:id>', views.category_detail),
	path('category', views.category_list),
	path('product', views.product_list),
	path('product/<int:id>', views.product_detail),
	path('product_category/<int:id>', views.product_category_detail),
	path('product_category', views.product_category_list),
	#path('category_product', views.category_product_list),
]
