from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from shop.models import Product, Category, Subcategory

from .cart import Cart

@require_GET
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product, quantity=1, update_quantity=False)
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request, 'cart.html', {'cart': cart, 'categories': categories, 'subcategories': subcategories})
