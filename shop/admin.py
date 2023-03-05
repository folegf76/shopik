from django.contrib import admin
from .models import Category, Product, Subcategory, Brand, ProductsPhoto
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'is_visible', 'created', 'updated', 'on_sale']
    list_filter = ['is_visible', 'created', 'updated']
    list_editable = ['price', 'is_visible']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'position', 'description']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'position']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visible', 'position', 'category']
    list_filter = ['is_visible', 'position', 'category']
    list_editable = ['is_visible', 'position', 'category']


@admin.register(ProductsPhoto)
class ProductsPhotoAdmin(admin.ModelAdmin):
    list_display = ['id_product', 'image']
    list_filter = ['id_product']
    list_editable = ['image']