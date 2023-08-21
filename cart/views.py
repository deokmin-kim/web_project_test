from django.shortcuts import render, redirect, get_object_or_404
from product.models import Product
from .models import CartItem
from django.contrib.auth.decorators import login_required

@login_required
def add_to_cart(request, product_id): # product_id는 URL에서 받아오는 상품의 고유 ID입니다.
    product = get_object_or_404(Product, pk=product_id)
    # get_object_or_404 함수를 사용하여  데이터베이스에서 Product 모델 중에서 pk 값이 product_id와 일치하는 상품을 가져오거나, 상품이 존재하지 않으면 404 오류를 발생시킵니다
    # get_object_or_404: 데이터베이스에서 객체를 가져오거나, 해당 객체가 없으면 404 오류를 발생시킵니다.
    user = request.user # request.user는 현재 로그인한 사용자를 나타냅니다.

    cart_item, created = CartItem.objects.get_or_create(user=user, product=product, quantity=1)
    # CartItem 모델의 objects 매니저를 통해 사용자와 상품 정보에 해당하는 장바구니 아이템을 가져오거나 생성합니다.
    # get_or_create 메서드는 아이템이 이미 존재하면 가져오고, 없으면 새로 생성합니다.
    # 현재 로그인한 사용자가 user로 설정됩니다.
    # get_object_or_404를 사용하여 가져온 상품 객체가 product로 설정됩니다.
    # quantity=1: 이 부분은 CartItem 모델의 quantity 필드를 지정하는 것으로, 장바구니에 추가되는 상품의 수량을 1로 설정합니다.
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    # 만약 created가 False인 경우(이미 장바구니에 아이템이 존재하는 경우), 해당 아이템의 수량을 1 증가시키고 저장합니다.
    return redirect('cart:cart_detail')

@login_required
def cart_detail(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)

    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})
