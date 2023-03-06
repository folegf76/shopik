from django.contrib import admin
from .models import Blog

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['name', 'author', 'position', 'is_visible', 'created']
    list_filter = ['is_visible', 'author', 'created']
    list_editable = ['is_visible', 'position']
