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
		fields = ['id','name','unit_price','slug','description','inventory','unit_price_taxed','category']
	
	unit_price_taxed = serializers.SerializerMethodField(method_name='calculate_tax')
	def calculate_tax(self, product: Product):
		return product.unit_price * Decimal(1.1)

class CategoryCountSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name','position','products_count']

	products_count = serializers.IntegerField(read_only=True)

class CategoryProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name','position','products']
	products = ProductSerializer()

class ProductCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = ['id','name','unit_price','category']
	category = CategorySerializer()

