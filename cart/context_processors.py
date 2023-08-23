from cart.models import CartItem  # 임포트 필요한 모델

def cart_item_count(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    cart_item_count = cart_items.count()  # 장바구니에 담긴 상품 개수 계산
    return {'cart_item_count': cart_item_count}