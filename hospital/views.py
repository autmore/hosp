from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import Group, User

from . import forms, models
from .forms import AuthenticateForm
from hospital.urls import *


# bQ5n5EAT2CexLGm


def main(request):
    return render(request, template_name="main/index.html")


class RegisterUser(CreateView):
    form_class = forms.SignUpForm
    template_name = 'main/registration.html'
    success_url = reverse_lazy('login')
    context_object_data = 'Регистрация'


class LoginUser(BaseLoginView):
    template_name = "main/login.html"
    form_class = AuthenticateForm
    success_url = reverse_lazy('index')
    context_object_data = 'Вход'

    def get_success_url(self):
        return self.success_url


class LogoutUser(LogoutView):
    success_url = reverse_lazy('index')

    def get_success_url(self):
        return self.success_url


def connect_user_to_doctors(request):
    try:
        # Получаем пользователя по его ID
        user = User.objects.get(id=request.user.id)

        # Получаем группу по имени
        group = Group.objects.get(name='doctor')

        # Добавляем пользователя в группу
        user.groups.add(group)

        # Сохраняем изменения
        user.save()
        print(f"Пользователь {user.username} успешно добавлен в группу doctor")

        # Перенаправляем пользователя после добавления в группу
        return redirect('index')  # Перенаправление на главную страницу (или на другую страницу)

    except User.DoesNotExist:
        print("Пользователь не найден")
        return redirect('error_page')  # Перенаправление на страницу ошибки, если пользователь не найден
    except Group.DoesNotExist:
        print("Группа не найдена")
        return redirect('error_page')

def profile(request):
    try:
       group = Group.objects.filter(user__id=request.user.id)
    except Group.DoesNotExist:
        group = None
    for gr in group:
        if gr.name == "doctor":
            pass
        elif gr.name == "nurse":
            pass
        else:
            diagnosis = models.Diagnosis.objects.filter(doctor_id=request.user.id)
            heal = models.Heal.objects.all()
            return render(request, 'main/user_profile.html', locals())
    return render(request, 'main/user_profile.html', locals())

