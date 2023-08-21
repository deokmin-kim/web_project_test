from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='상품명') # 문자열 필드
    price = models.IntegerField(verbose_name='상품가격') # 정수 필드
    description = models.TextField(verbose_name='상품설명') # 텍스트 필드
    stock = models.IntegerField(verbose_name='재고') # 정수 필드
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
    # 상품이 등록된 날짜와 시간을 나타내는 날짜 및 시간 필드입니다.
    # auto_now_add 매개변수가 True로 설정되어 있으므로, 새 상품이 생성될 때 자동으로 등록 시간이 설정됩니다.
    def __str__(self):
        return self.name
    # __str__ 메서드는 객체를 문자열로 나타낼 때 사용됩니다. 이 메서드가 정의되면,
    # 객체를 문자열로 표현할 때 self.name이 사용됩니다.
    # 즉, 상품 객체가 문자열로 표시될 때는 해당 상품의 이름이 사용됩니다.

    class Meta:
    	db_table = 'my_product'
    	verbose_name = '상품'
    	verbose_name_plural = '상품'
        # db_table은 실제 데이터베이스 테이블의 이름을 설정하고,
        # verbose_name과 verbose_name_plural은 모델의 단수와 복수형 표시 이름을 설정합니다.