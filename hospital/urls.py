from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views
from hospital.views import *

urlpatterns = [
    path("", views.main, name="index"),
    path("user/registration/", RegisterUser.as_view(), name="registration"),
    path("user/login/", LoginUser.as_view(), name="login"),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('con_to_group/', connect_user_to_doctors, name='con_to_group'),
    path('profile/', profile, name='profile'),
]