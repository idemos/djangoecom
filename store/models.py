from django.db import models

# Create your models Category.
class Category(models.Model):
    image = models.ImageField(upload_to='store/images', null=True, blank=True)
    name = models.CharField(max_length=255)
    position = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['name']

# Create your models Product.
class Product(models.Model):
    image = models.ImageField(upload_to='store/images', null=True, blank=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    # ordinamento di default
    class Meta:
        ordering = ['name']


class Customer(models.Model):
    name = models.CharField(max_length=255)
    piva = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['created_at']


class User(models.Model):
    SEX_MALE = 'M'
    SEX_FEMALE = 'F'

    SEX_CHOICES = [
        (SEX_MALE, 'Maschio'),
        (SEX_FEMALE, 'Femmina'),
    ]

    firstname = models.TextField(max_length=255)
    lastname = models.TextField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default=SEX_MALE)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.firstname} {self.lastname}'

    class Meta:
        ordering = ['firstname','lastname']

# Create your models Order.
class Order(models.Model):
    #id = models.AutoField(primary_key=True)
    anno = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)