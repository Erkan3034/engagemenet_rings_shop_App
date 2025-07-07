from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products_list, name='products_list'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('api/products/', views.api_products, name='api_products'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
] 