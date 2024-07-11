from django.urls import path
from .views import *

urlpatterns = [
    path("", training_log_method),
    path("list/", training_log_list),
    path("delete/", training_log_delete),
]