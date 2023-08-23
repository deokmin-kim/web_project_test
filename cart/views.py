from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import CartItem
from django.contrib.auth.decorators import login_required

# 0823 cart에 add할때 중복문제로 수정
@login_required
def add_to_cart(request, product_id): # product_id는 URL에서 받아오는 상품의 고유 ID입니다.
    user = request.user
    product = Product.objects.get(id=product_id)

    # 이미 장바구니에 동일한 제품이 있는지 확인
    cart_item = CartItem.objects.filter(user=user, product=product).first()

    if cart_item:
        # 이미 있는 경우: 수량 증가
        cart_item.quantity += 1
        cart_item.save()
    else:
        # 없는 경우: 새로운 아이템 생성
        new_cart_item = CartItem(user=user, product=product, quantity=1)
        new_cart_item.save()

    return redirect('cart:cart_detail')  # 장바구니 페이지로 리다이렉트

@login_required
def cart_detail(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    # 0823 cartlist에 정적페이지 -> 동적페이지로 수정
    # 각 cart_item의 total_price를 계산하여 추가합니다.
    for cart_item in cart_items:
        cart_item.total_price = cart_item.product.price * cart_item.quantity

    total_price = sum(cart_item.total_price for cart_item in cart_items)

    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def checkout_cart(request): # main_page 함수는 웹사이트의 메인 페이지를 렌더링하는 부분입니다.
    user = request.user
    cart_items = CartItem.objects.filter(user=user)

    # 각 cart_item의 total_price를 계산하여 추가합니다.
    for cart_item in cart_items:
        cart_item.total_price = cart_item.product.price * cart_item.quantity

    total_price = sum(cart_item.total_price for cart_item in cart_items)

    return render(request, 'cart/checkout.html', {'cart_items': cart_items, 'total_price': total_price})

# 0823 장바구니 삭제하는 view항목 추가
@login_required
def remove_from_cart(request, product_id):
    user = request.user
    product = Product.objects.get(id=product_id)

    # 해당 제품에 대한 장바구니 아이템 삭제
    cart_item = CartItem.objects.filter(user=user, product=product).first()
    if cart_item:
        cart_item.delete()

    return redirect('cart:cart_detail')  # 장바구니 페이지로 리다이렉트