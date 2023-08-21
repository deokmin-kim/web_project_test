from django.shortcuts import render, get_object_or_404, redirect
from .models import Order
from product.models import Product
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# get_user_model(): 이 함수는 현재 사용되고 있는 사용자 모델 클래스를 가져옵니다.
@login_required
def create_order(request):
    if request.method == 'POST':
        # username=request.user.username: 로그인한 사용자의 사용자 이름(유저네임)을 가지고 오는 부분입니다.
        # get() 메서드는 데이터베이스에서 특정 조건을 만족하는 객체를 가져옵니다.
        user = get_user_model().objects.get(username=request.user.username)  # 로그인한 사용자를 가져옴
        product_id = request.POST.get('product_id')  # 상품 ID를 POST 데이터로 받음
        quantity = int(request.POST.get('quantity', 1))  # POST 데이터에서 'quantity' 파라미터 값을 가져오는데, 값이 없을 경우 기본값으로 1을 사용합니다.

        if not product_id:
            messages.error(request, "상품 ID가 유효하지 않습니다.")
            return redirect('order:create_order') # 상품 ID가 없을 경우, 오류 메시지를 생성하고 'order:create_order' URL로 리다이렉트합니다.

        try:
            product = Product.objects.get(pk=int(product_id)) # 상품 ID가 유효한지 확인하고, Product 모델을 통해 해당 상품을 가져옵니다.
        except (Product.DoesNotExist, ValueError):
            messages.error(request, "유효하지 않은 상품 ID입니다.")
            return redirect('order:create_order')
        order = Order.objects.create(user=user, product=product, quantity=quantity)

        # 상품과 사용자 정보를 기반으로 주문 생성
        # product = get_object_or_404(Product, pk=product_id)
        # order = Order.objects.create(user=user, product=product, quantity=quantity)

        # 주문 생성 후 처리 로직
        messages.success(request, "주문이 성공적으로 생성되었습니다.")
        return render(request, 'order/created.html', {'order': order})
    else:
        # GET 요청에 대한 처리
        products = Product.objects.all()  # 상품 목록을 가져옴
        context = {'products': products}  # 템플릿에 전달할 컨텍스트
        # 상품 선택 및 수량 입력하는 폼을 보여줄 수 있음
        return render(request, 'order/create.html',context)

def view_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    return render(request, 'order/view.html', {'order': order})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})
