from django.contrib import admin
from .models import Category, Product, Subcategory, Brand, ProductsPhoto
# Register your models here.

admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Subcategory)
admin.site.register(Brand)
admin.site.register(ProductsPhoto)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'is_visible', 'created', 'updated', 'on_sale']
    list_filter = ['is_visible', 'created', 'updated']
    list_editable = ['price', 'is_visible']
    prepopulated_fields = {'slug': ('name',)}