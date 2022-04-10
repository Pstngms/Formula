

from django.contrib.auth import login, logout
from django.http import HttpResponseNotFound, HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from accounts.forms import UserRegisterForm, UserLoginForm, UserUpdateForm

from django.contrib import messages

from accounts.models import CustomUser


def profile(request):
    return render(request, 'accounts/profile.html')


def profile_update(request,id):
    try:
        form = CustomUser.objects.get(id=id)
        if request.method == 'POST':
            form.first_name = request.POST.get('first_name')
            form.last_name = request.POST.get('last_name')
            form.patronymic = request.POST.get('patronymic')
            form.email = request.POST.get('email')
            form.phone = request.POST.get('phone')
            form.vk_link = request.POST.get('vk_link')
            form.save()
            return HttpResponseRedirect("/profile")
        else:
            return render(request, 'accounts/profile_update.html', {"form": form})
    except CustomUser.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")




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
