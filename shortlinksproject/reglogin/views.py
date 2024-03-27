from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth import login, logout


def register(request):
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно')

            user = form.save()
            login(request, user)
        else:
            messages.error(request, 'Ошибка регистрации')

    else:
        form = UserRegisterForm()
    return render(request, 'reglogin/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        current_user = request.user
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_links', current_user.id)
    else:
        form = UserLoginForm()
    return render(request, 'reglogin/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('Login')
