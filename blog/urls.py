from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_view, name='blog'),
    path('<int:id>/', views.blog_details, name='blog_details'),
]