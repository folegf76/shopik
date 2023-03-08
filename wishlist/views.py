from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET

from shop.models import Product, Category, Subcategory

from .wish import Wish

@require_GET
def wish_add(request, product_id):
    wish = Wish(request)
    product = get_object_or_404(Product, id=product_id)
    wish.add(product=product)
    return redirect('wishlist:wish_detail')

def wish_remove(request, product_id):
    wish = Wish(request)
    product = get_object_or_404(Product, id=product_id)
    wish.remove(product)
    return redirect('wishlist:wish_detail')

def wish_detail(request):
    wish = Wish(request)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request, 'wishlist.html', {'wish': wish, 'categories': categories, 'subcategories': subcategories})

