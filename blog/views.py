from django.shortcuts import render, get_object_or_404
from shop.models import Category, Subcategory
from blog.models import Blog
# Create your views here.


def blog_view(request):
    blogs = Blog.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'blog.html',
                  {'blogs': blogs,
                   'categories': categories,
                   'subcategories': subcategories},
                  )


def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id, is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'blog-details.html',
                  {'blog': blog,
                   'categories': categories,
                   'subcategories': subcategories},
                  )
