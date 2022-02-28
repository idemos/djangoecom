from decimal import Decimal
from rest_framework import serializers
from .models import CartItem, Category, Product, Review, Cart


class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		model = Review
		fields = ['id','name','description','created_at','product']

class CategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Category
		fields = ['id','name','position']

class ProductSerializer(serializers.ModelSerializer):
	unit_price_taxed = serializers.SerializerMethodField(method_name='calculate_tax')
	class Meta:
		model = Product
		fields = ['id','name','unit_price','slug','description','inventory','unit_price_taxed','category']
	
	def calculate_tax(self, product: Product):
		return product.unit_price * Decimal(1.1)

class CategoryCountSerializer(serializers.HyperlinkedModelSerializer):
	products_count = serializers.IntegerField(read_only=True)
	class Meta:
		model = Category
		fields = ['id','name','position','products_count']


class CategoryProductSerializer(serializers.ModelSerializer):
	products = ProductSerializer()
	class Meta:
		model = Category
		fields = ['id','name','position','products']

class ProductCategorySerializer(serializers.ModelSerializer):
	category = CategorySerializer()
	class Meta:
		model = Product
		fields = ['id','name','unit_price','category']

class CartItemSerializer(serializers.ModelSerializer):
	product = ProductSerializer()
	total_price = serializers.SerializerMethodField(method_name='calculate_total_price')

	def calculate_total_price(self, cart_item: CartItem):
		return cart_item.product.unit_price * cart_item.quantity
	class Meta:
		model = CartItem
		fields = ['id','quantity','product','total_price']	

class CartSerializer(serializers.ModelSerializer):
	# puo solo leggere e non puo invaire al server
	# la uuid, cosi togliamo dalla web api la proprieta id
	id=serializers.UUIDField(read_only=True)
	cartitems = CartItemSerializer(many=True,read_only=True)

	total_price = serializers.SerializerMethodField(method_name='calculate_total_price')

	def calculate_total_price(self, cart: Cart):
		return sum([item.quantity * item.product.unit_price for item in cart.cartitems.all()])

	class Meta:
		model = Cart
		#fields = ['id']
		#cartitems +è il nome della relazione relation_name
		fields = ['id','cartitems','total_price']
		#fields = ['id','cartitems']
