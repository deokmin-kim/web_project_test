from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('create/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.view_order, name='view_order'), # 주문 정보를 표시
    path('orderlist/', views.order_list, name='order_list'),  # 주문 목록을 표시하는 URL 패턴 추가

    path('notices/', views.notice_list, name='notice_list'),
    path('notices/<int:notice_id>/', views.notice_detail, name='notice_detail'),
    # 다른 주문 관련 URL 패턴들도 추가할 수 있습니다.
]
