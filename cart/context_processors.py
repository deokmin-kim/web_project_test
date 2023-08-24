from cart.models import CartItem  # 임포트 필요한 모델

def cart_item_count(request):
    user = request.user
    if user.is_authenticated:  # 사용자가 로그인한 경우에만 카트 아이템 개수를 조회
        cart_items = CartItem.objects.filter(user=user)
        cart_item_count = cart_items.count()
    else:
        cart_item_count = 0  # 로그인하지 않은 경우에는 카트 아이템 개수를 0으로 설정
    return {'cart_item_count': cart_item_count}