from django.contrib import admin
from user.models import User

class UserAdmin(admin.ModelAdmin): # user 모델에 대한 관리자 페이지 설정을 담당
    list_display = ('email',) # 해당 관리자 페이지에서 이메일을 보여주게함.
    # # 마지막에 , 안 넣으면 문자열로 인식한다.

admin.site.register(User, UserAdmin)