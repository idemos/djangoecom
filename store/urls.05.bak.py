from django.urls import path
from . import views

urlpatterns = [
	path('category/', views.CategoryList.as_view()),
	path('category/<int:pk>', views.CategoryDetail.as_view()),
	path('product/', views.ProductList.as_view()),
	path('product/<int:pk>', views.ProductDetail.as_view()),
	path('product_category/<int:id>', views.product_category_detail),
	path('product_category/?$', views.product_category_list),
]
