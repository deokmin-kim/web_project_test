from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'product'

urlpatterns = [
    path('', views.main_page, name='home'),
    path('home/', views.main_page, name='index'),
    path('list/', views.product_list, name='product-list'),
    path('list/<int:pk>/', views.product_detail, name='product-detail'),
    path('contact/', views.contact_page, name='contact'),
    path('shop/', views.shop_page, name='shop'),
    path('shop_detail/', views.shop_detail_page, name='shop_detail'),
    path('products/carousel/', views.product_carousel, name='product_carousel'),
    path('search/', views.search_results, name='results'),
    # 상품 목록 forms.py만들고 하려다 실패
    # path('product/upload/', views.product_registration, name='product_registration'),
    # path('product/upload/success/', views.product_registration_success, name='upload_image_success'),
]

if settings.DEBUG: # 이게 있어야 관리자 페이지에서 이미지 클릭했을때 이미지가 보임
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urls.py에 미디어 URL 패턴 추가하기:
# 프로젝트의 urls.py 파일에 다음과 같이 URL 패턴을 추가해야 합니다.
# 이렇게 하면 개발 서버에서 미디어 파일을 서빙할 수 있게 됩니다.
# 위의 작업을 수행하고 나면, 미디어 파일이 제대로 서빙되어 관리자 페이지에서 이미지를 클릭했을 때 정상적으로 보여지게 될 것입니다.

