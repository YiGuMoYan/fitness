from django.urls import path
from .views import *

urlpatterns = [
    path("list/", get_comment),
    path("add/", add_comment),
]