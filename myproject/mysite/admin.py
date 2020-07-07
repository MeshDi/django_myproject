from django.contrib import admin
from.models import Product,Category


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'is_active','category']
    list_filter = ['is_active','category']
    list_editable = ['is_active']
    search_fields = ('name','desc','category__name')


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    pass