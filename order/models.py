from django.db import models
from django.contrib.auth.models import User  # 이 부분을 추가

class Order(models.Model): # 데이터베이스의 테이블과 필드를 정의하는 역할을 합니다.
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, verbose_name='사용자인듯')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='상품')
    # on_delete=models.CASCADE 옵션은 해당 사용자가 삭제될 경우 관련된 주문도 함께 삭제되도록 설정하는 것을 의미합니다.
    # verbose_name은 관리자 페이지(url/admin)에서 이 필드가 어떻게 표시될지를 지정합니다.
    quantity = models.IntegerField(verbose_name='수량')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    # 이 필드는 auto_now_add=True 설정이 되어있어 객체가 생성될 때 현재 날짜와 시간이 자동으로 기록됩니다

    def __str__(self):
        return f"Order {self.id}"  # 주문 객체를 "Order 주문ID" 형식으로 표시
        # 이렇게 하면 관리자 페이지에서 주문 객체를 목록에서 볼 때 보다 읽기 쉬운 형태로 표시됩니다.
    class Meta: # class Meta 부분의 설정들은 주문 모델을 관리자 페이지에서 어떻게 표시하고 조작할지를 제어합니다
        db_table = 'my_order' # DB에 저장될 테이블 이름 지정
        # 이 설정은 모델의 별칭을 지정하는 것으로 verbose_name = '주문'과
        # verbose_name_plural = '주문'으로 설정하면, 관리자 페이지에서 "주문"으로 표시됩니다.
        verbose_name = '주문임'
        verbose_name_plural = '주문임'
        # 복수형 지정안하면 "주문s"가 되는데요. s붙이지 않기 위해서 그렇다.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title