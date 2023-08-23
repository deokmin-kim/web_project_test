from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm

def sign_up(request):
    if request.method == 'GET':
        form = RegisterForm() # get일때는 기본 생성자
        return render(request, 'user/register.html', {'form': form})
    elif request.method == 'POST':
        form = RegisterForm(request.POST) # post일때는 매개인자 있는 생성자
        if form.is_valid():
            user = form.save(commit=False) # 바로 저장하지 않고
            user.username = user.username.lower() # username 들어오면 이름을 소문자로 바꾸어서
            user.save() # 이름 저장
            messages.success(request, "You have Signed up successfully.")
            login(request,user)
            return redirect('/')
        else:
            return render(request, 'user/register.html', {'form': form})

def sign_in(request):
    if request.method == 'GET':
        form = LoginForm() # get일때는 기본 생성자
        return render(request, 'user/login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST) # post일때는 매개인자 있는 생성자
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(
                    request, f'Hi {username.title()}, welcome back!')
                return redirect('user:home')

        # 유효하지 않거나 사용자가 인증 되지 않을 경우
        messages.error(request, f'Invalid username or password')
        return render(request, 'user/login.html', {'form': form})

def sign_out(request):
    logout(request)
    messages.success(request, f'You have been logged out.')
    return redirect('user:home')


def home(request):
    return render(request, 'product/index.html')
