from django.contrib import admin # 장고의 admin 앱에서 관리자 페이지 기능을 사용하기 위해 필요한 admin 모듈을 불러오는 부분입니다.
from order.models import Order
from order.models import Notice

class OrderAdmin(admin.ModelAdmin): # 이 클래스는 Order 모델에 대한 관리자 페이지 설정을 담당합니다. admin.ModelAdmin 클래스를 상속받아서 새로운 설정을 추가할 수 있습니다.
    list_display = ('user', 'product',)
    # list_display는 튜플로 구성된 필드명을 가지며, 이에 해당하는 필드들이 관리자 페이지의 리스트 뷰에 표시됩니다.
    # 위의 코드에서는 'user'와 'product' 필드가 리스트 뷰에 표시되도록 설정되어 있습니다.
admin.site.register(Order, OrderAdmin)
# 이 코드는 Order 모델을 OrderAdmin 클래스를 사용하여 관리자 페이지에 등록하는 부분입니다.
# 이를 통해 관리자 페이지에서 Order 모델에 대한 설정이 적용됩니다.
# 등록된 모델은 관리자 페이지에서 해당 모델을 관리할 수 있는 인터페이스가 생성됩니다.

admin.site.register(Notice)