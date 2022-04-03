from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from accounts.forms import UserRegisterForm, UserLoginForm

from django.contrib import messages

def profile(request):
    return render(request, 'accounts/profile.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
    else:

        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {"form": form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно авторизировались')
            return redirect('news')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {"form": form})


def user_logout(request):
    logout(request)
    return redirect('login')
