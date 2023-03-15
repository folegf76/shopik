from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'address_city', 'postal_code', 'address_street', 'address_apartment', 'created', 'updated']
    list_filter = ['email', 'created', 'updated']
    inlines = [OrderItemInline]

