from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cartlist/', views.cart_detail, name='cart_detail'),
    path('checkout/', views.checkout_cart, name='checkout'),
    # 0823 장바구니 삭제 url매핑
    path('remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
]
