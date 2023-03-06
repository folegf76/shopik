from django.contrib import admin
from .models import AboutGallery, WhatCan, CustomersSays, OurPluses
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
