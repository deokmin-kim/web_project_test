from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.main_page, name='home'),
    path('list/', views.product_list, name='product-list'),
    path('list/<int:pk>/', views.product_detail, name='product-detail'),
]
