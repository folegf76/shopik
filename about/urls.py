from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about_views, name='about'),
    path('services/', views.services_views, name='services'),
    path('faq/', views.faq_views, name='faq'),
]