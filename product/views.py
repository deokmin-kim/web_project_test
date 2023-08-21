from django.shortcuts import render, get_object_or_404
from .models import Product

def main_page(request): # main_page 함수는 웹사이트의 메인 페이지를 렌더링하는 부분입니다.
    return render(request, 'product/index.html')

def product_list(request): # product_list 함수는 모든 상품을 리스트 형태로 렌더링하는 부분입니다.
    products = Product.objects.all()
    return render(request, 'product/product_list.html', {'products': products})
    # Product.objects.all()은 데이터베이스에서 모든 Product 객체를 가져오는 쿼리를 수행합니다.
    # 이렇게 가져온 상품 객체들은 'product/product_list.html' 템플릿에 'products'라는 이름으로 전달되어 렌더링됩니다.
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/product_detail.html', {'product': product})
    # get_object_or_404(Product, pk=pk)는 데이터베이스에서 주어진 기본 키에 해당하는 Product 객체를 가져오거나,
    # 해당 객체가 존재하지 않을 경우 404 오류를 발생시킵니다.
    # 이렇게 가져온 상품 객체는 'product/product_detail.html' 템플릿에 'product'라는 이름으로 전달되어 렌더링됩니다.

def contact_page(request):
    return render(request, 'product/contact.html')

def shop_page(request):
    return render(request, 'product/shop.html')

def shop_detail_page(request):
    return render(request, 'product/detail.html')