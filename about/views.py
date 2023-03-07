from django.shortcuts import render, get_object_or_404
from shop.models import Category, Subcategory
from .models import OurPluses, CustomersSays, WhatCan, AboutGallery, ImgServices, PriceServices, Faq
# Create your views here.


def about_views(request):
    our_pluses = OurPluses.objects.filter(is_visible=True)
    about_gallery = AboutGallery.objects.filter(is_visible=True)
    what_can = WhatCan.objects.filter(is_visible=True)
    customers_saya = CustomersSays.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)
    return render(request,
                  'about.html',
                  {'our_pluses': our_pluses,
                   'about_gallery': about_gallery,
                   'what_can': what_can,
                   'customers_saya': customers_saya,
                   'categories': categories,
                   'subcategories': subcategories},
                  )


def services_views(request):
    img_s = ImgServices.objects.filter(is_visible=True)
    prices = PriceServices.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)

    return render(request, 'services.html',
                  {'img_s': img_s,
                   'prices': prices,
                   'categories': categories,
                   'subcategories': subcategories},
                 )

def faq_views(request):
    faq_s = Faq.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    subcategories = Subcategory.objects.filter(is_visible=True)

    return render(request, 'faq.html',
                  {'faq_s': faq_s,
                   'categories': categories,
                   'subcategories': subcategories},
                 )


