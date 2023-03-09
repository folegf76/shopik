from django.shortcuts import render, get_object_or_404
from shop.models import Category, Subcategory
from blog.models import Blog
from cart.cart import Cart
# Create your views here.


def blog_view(request):
    cart = Cart(request)
    blogs = Blog.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'blog.html',
                  {'blogs': blogs,
                   'cart': cart,
                   'categories': categories,
                   'subcategories': subcategories},
                  )


def blog_details(request, id):
    cart = Cart(request)
    blog = get_object_or_404(Blog, id=id, is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'blog-details.html',
                  {'blog': blog,
                   'cart': cart,
                   'categories': categories,
                   'subcategories': subcategories},
                  )
