from django import forms
from django.contrib.auth.models import User # 내장된 테이블 User , 얘를 어디서 테스트 해봤냐면 127.0.0.1:8000/admin -> 계정생성
from django.contrib.auth.forms import UserCreationForm # 내장된 폼

# db연결안할거니까 Model 없음
class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
