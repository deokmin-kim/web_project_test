from django.db import models
#from django.contrib.auth.models import AbstractUser, Group, Permission

# class User(AbstractUser):
#     created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜')
class User(models.Model):
    email = models.EmailField(verbose_name='이메일') # 관리자 화면에서 고객 추가할때 보임
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    created_dt = models.DateTimeField(auto_now_add=True, verbose_name='등록날짜') # 처음 객체가 생성된 날짜를 자연스럽게 지정하기 위해 auto_now_add로 지정해요.

    def __str__(self):
        return self.email

    class Meta:
    	db_table = 'my_user'
    	verbose_name = '고객'
    	verbose_name_plural = '고객'

# 충돌을 피하기 위해 related_name 추가
# class CustomGroup(Group):
#     class Meta:
#         proxy = True
#
# # 충돌을 피하기 위해 related_name 추가
# class CustomPermission(Permission):
#     class Meta:
#         proxy = True