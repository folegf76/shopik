from django.contrib import admin
from .models import AboutGallery, WhatCan, CustomersSays, OurPluses, OurServices, ImgServices, PriceServices, Faq
# Register your models here.


@admin.register(OurPluses)
class OurPluses(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'description']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']


@admin.register(AboutGallery)
class AboutGallery(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'description']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']


@admin.register(WhatCan)
class WhatCan(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']


@admin.register(CustomersSays)
class CustomersSays(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'description']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']

@admin.register(OurServices)
class OurServices(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'description']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']

@admin.register(ImgServices)
class ImgServices(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'description']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']

@admin.register(PriceServices)
class PriceServices(admin.ModelAdmin):
    list_display = ['name', 'position', 'is_visible', 'price']
    list_filter = ['is_visible', 'position', 'price']
    list_editable = ['is_visible', 'position', 'price']


@admin.register(Faq)
class Faq(admin.ModelAdmin):
    list_display = ['question', 'position', 'is_visible', 'answer']
    list_filter = ['is_visible', 'position']
    list_editable = ['is_visible', 'position']