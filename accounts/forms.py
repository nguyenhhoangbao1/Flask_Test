from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

# Form đăng ký người dùng
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Form đăng nhập
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
