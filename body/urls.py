from django.urls import path
from .views import *

urlpatterns = [
    path("", body_method),
    path("list/", get_list),
    path("update/", update),
    path("delete/", delete),
]