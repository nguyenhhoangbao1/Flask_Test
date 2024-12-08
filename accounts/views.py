from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegisterForm, LoginForm

# Đăng ký người dùng
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Đăng nhập sau khi đăng ký thành công
            messages.success(request, 'Đăng ký thành công!')
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Đăng nhập người dùng
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Đăng nhập thành công!')
            return redirect('profile')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# Đăng xuất người dùng
def logout_view(request):
    logout(request)
    messages.info(request, 'Bạn đã đăng xuất!')
    return redirect('login')

# Trang cá nhân người dùng
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})
