from django.urls import path
from .views import *

urlpatterns = [
    path("list/", food_list)
]