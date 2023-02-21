from django.urls import path
from . import views

app_name = 'shop'

urlpatterns = [
    path('', views.shop),
    # path('', views.product_list, name='product_list'),
    # path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]