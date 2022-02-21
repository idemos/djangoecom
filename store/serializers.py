from decimal import Decimal
from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name','position']

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id','name','unit_price','unit_price_taxed','category']
	
	unit_price_taxed = serializers.SerializerMethodField(method_name='calculate_tax')
	def calculate_tax(self, product: Product):
		return product.unit_price * Decimal(1.1)


class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id','name','unit_price','category']
	category = CategorySerializer()

# class CategoryProductSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Category
# 		fields = ['id','name','position','products']
# 	products = ProductSerializer()