from django.urls import path
from . import views

urlpatterns = [
    path('', views.toko, name="toko"),
    path('search/', views.search, name="search"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('kontak/', views.kontak, name="kontak"),
    path('detail/', views.detail, name="detail"),
 
]