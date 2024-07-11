from django.urls import path
from .views import *

urlpatterns = [
    path("", diet_method),
    path("list/", get_list),
    path("update/", update),
    path("delete/", delete),
]