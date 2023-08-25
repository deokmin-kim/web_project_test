from django.db import models
from django.contrib.auth.models import User # Django의 내장된 User 모델을 가져옵니다.
# 사용자 이름, 비밀번호, 이메일 등을 포함하여 사용자 정보를 다루는 데 사용됩니다.
from product.models import Product

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # User는모델과의 관계를 나타내며, on_delete=models.CASCADE는 해당 사용자가 삭제될 때 이 아이템도 함께 삭제되어야 함을 의미합니다.
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField() # quantity 필드는 장바구니 아이템에 담긴 상품의 수량을 나타냅니다.
    # models.PositiveIntegerField()는 양의 정수 필드를 나타냅니다. 수량은 0보다 크거나 같은 정수여야 합니다.

    # 0825 size 때문에 코드추가
    size = models.CharField(max_length=10, verbose_name='Size', choices=[
        ('230', '230'),
        ('240', '240'),
        ('250', '250'),
        ('260', '260'),
        ('270', '270'),
    ])  # 사이즈 필드 추가

    # def __str__(self):
    #     return f"{self.user.username} - {self.product.name} ({self.quantity}개)"
        # 장바구니 아이템을 사용자 이름, 상품 이름 및 수량과 함께 나타내는 형식으로 문자열로 표현합니다.

    # 0825 코드 수정
    def __str__(self):
        return f"{self.user.username} - {self.product.name} ({self.quantity}개) - Size: {self.size}"
        # 장바구니 아이템을 사용자 이름, 상품 이름 및 수량과 함께 나타내는 형식으로 문자열로 표현합니다.