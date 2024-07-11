from django.urls import path
from .views import *

urlpatterns = [
    path("login/", login),
    path("signup/", signup),
    path("", account_method),
    path("update_password/", update_password),
]