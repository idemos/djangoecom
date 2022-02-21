from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    #category è il nome del model
    list_display = ['name', 'unit_price', 'inventory_status', 'category']
    list_editable = ['unit_price']
    list_per_page = 20

#    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if(product.inventory < 10):
            return 'low'
        return 'good'


# Register your models here.
# admin.site.register(models.Product, models.ProductAdmin)

# admin.site.register(models.Category)

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
    list_editable = ['position']
    list_per_page = 20


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 20
