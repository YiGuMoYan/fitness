from django.urls import path
from .views import *

urlpatterns = [
    path("list/", get_fit_list)
]