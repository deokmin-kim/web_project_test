from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.main_page, name='home'),
    path('list/', views.product_list, name='product-list'),
    path('list/<int:pk>/', views.product_detail, name='product-detail'),
    path('contact/', views.contact_page, name='contact'),
    path('shop/', views.shop_page, name='shop'),
    path('shop_detail/', views.shop_detail_page, name='shop_detail'),
]
