from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.db.models import Q
from .forms import ProductForm
from django.contrib import messages
from django.core.paginator import Paginator

def main_page(request): # main_page 함수는 웹사이트의 메인 페이지를 렌더링하는 부분입니다.
    # products = Product.objects.all()
    # return render(request, 'product/index.html', {'products': products})
    # 0824 수정
    search_query = request.GET.get('search')  # 검색어 가져오기

    if search_query:  # 검색어가 있을 경우
        products = Product.objects.filter(name__icontains=search_query)  # 검색어를 포함하는 상품 필터링
    else:
        products = Product.objects.all()  # 검색어가 없을 경우 모든 상품 가져오기

    return render(request, 'product/shop.html', {'products': products})


def contact_page(request):
    return render(request, 'product/contact.html')


def shop_page(request):  # product_list 함수는 모든 상품을 리스트 형태로 렌더링하는 부분입니다.
    products = Product.objects.all()

    #paging
    items_per_page = 15  # 한 페이지에 보여줄 항목 수
    paginator = Paginator(products, items_per_page)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    current_page = page.number

    context = {'products': products, 'page': page, 'current_page': current_page}
    return render(request, 'product/shop.html', context)
    # Product.objects.all()은 데이터베이스에서 모든 Product 객체를 가져오는 쿼리를 수행합니다.
    # 이렇게 가져온 상품 객체들은 'product/shop_page.html' 템플릿에 'products'라는 이름으로 전달되어 렌더링됩니다.

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/detail.html', {'product': product})

def shop_detail_page(request, pk):
    product = get_object_or_404(Product, pk=pk)
    sizes = product.sizes.all()
    context = {'product': product, 'sizes': sizes}
    return render(request, 'product/detail.html', context)


def search_results(request):
    query = request.GET.get('q')  # 검색어 가져오기
    products = Product.objects.filter(
        Q(name__icontains=query) |  # 제품명에 검색어 포함
        Q(description__icontains=query)  # 설명에 검색어 포함
    ).distinct()
    context = {'products': products, 'query': query}
    return render(request, 'product/search.html', context)


def product_carousel(request):
    products = Product.objects.all()  # 상품 데이터 가져오기
    return render(request, 'detail.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product/detail.html', {'product': product})