from django.contrib import admin
from product.models import Product


class ProductAdmin(admin.ModelAdmin): # product 모델에 대한 관리자 페이지 설정을 담당
    list_display = ('name', 'price',) # name : 상품명, price : 상품가격
    # 해당 관리자페이지 http://127.0.0.1:8000/admin/product/product/ 링크에 상품명과 상품가격을 표시됨

admin.site.register(Product, ProductAdmin)