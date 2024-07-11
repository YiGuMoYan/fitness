from django.urls import path
from .views import *

urlpatterns = [
    path("list/", get_gym_list),
    path("province/", get_province),
    path("city/", get_city)
]