from django.shortcuts import get_object_or_404, render
from cart.cart import Cart
from .models import Product, Category, Subcategory, Brand


def shop(request):
    cart = Cart(request)
    categories = Category.objects.filter(is_visible=True)
    sale_all = Product.objects.filter(on_sale=True)
    products = Product.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request, 'shop.html', context={
        'sale_all': sale_all,
        'products': products,
        'cart': cart,
        'categories': categories,
        'subcategories': subcategories,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'product-details.html',
                  {'product': product,
                   'categories': categories,
                   'subcategories': subcategories},
                  )

def shop_full(request, id):
    products = Product.objects.filter(is_visible=True, subcategory=id)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'shop-fullwidth.html',
                  {'products': products,
                   'categories': categories,
                   'subcategories': subcategories},
                  )