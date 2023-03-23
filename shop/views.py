from django.shortcuts import get_object_or_404, render
from cart.cart import Cart
from .models import Product, Category, Subcategory, Brand
from about.models import CustomersSays
from .forms import Search



def shop(request):
    cart = Cart(request)
    customers_saya = CustomersSays.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    sale_all = Product.objects.filter(on_sale=True)
    products = Product.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request, 'shop.html', context={
        'sale_all': sale_all,
        'customers_saya': customers_saya,
        'products': products,
        'cart': cart,
        'categories': categories,
        'subcategories': subcategories,
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    cart = Cart(request)
    return render(request,
                  'product-details.html',
                  {'product': product,
                   'categories': categories,
                   'cart': cart,
                   'subcategories': subcategories},

                  )


def shop_full(request, id, id_cat):
    products = Product.objects.filter(is_visible=True, subcategory=id)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    cart = Cart(request)
    return render(request,
                  'shop-fullwidth.html',
                  {'products': products,
                   'categories': categories,
                   'cart': cart,
                   'subcategories': subcategories},
                  )


def shop_category(request, id):
    products = Product.objects.filter(is_visible=True, subcategory__category=id)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    cart = Cart(request)
    return render(request,
                  'shop-fullwidth.html',
                  {'products': products,
                   'categories': categories,
                   'cart': cart,
                   'subcategories': subcategories},
                  )


def shop_search(request, sear):
    form = Search(request.POST or None)
    # sear1 = form.sear
    product_all = Product.objects.filter(is_visible=True)
    products = []
    sear = sear.lower()
    for produсt in product_all:
        prod = produсt.name.lower()
        if prod.find(sear) != -1:
            products.append(produсt)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    cart = Cart(request)
    return render(request,
                  'shop-fullwidth.html',
                  {'products': products,
                   'categories': categories,
                   'cart': cart,
                   'subcategories': subcategories},
                  )


