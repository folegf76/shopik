from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop, name='shop_list'),
    path('<int:id>/', views.shop_category, name='shop_category'),
    path('<int:id>/<int:id_cat>/', views.shop_full, name='shop_full'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]