from django.shortcuts import get_object_or_404, render

# from cart.cart import Cart
from .models import Product, Category, Subcategory, Brand


def shop(request):
    categories = Category.objects.filter(is_visible=True)
    sale_all = Product.objects.filter(on_sale=True)
    return render(request, 'shop.html', context={'sale_all': sale_all})


# def product_list(request, category_slug=None):
#     cart = Cart(request)
#     products = Product.objects.filter(available=True)
#     return render(request, 'list.html', {'products': products, 'cart': cart})
#
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request,
#                   'product_detail.html',
#                   {'product': product}
#                   )

