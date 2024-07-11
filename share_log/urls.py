from django.urls import path
from .views import *

urlpatterns = [
    path("upload/", upload),
    path("list/", get_list),
    path("delete/", delete),
    path("update/", update),
    path("view/", get_view_list),
    path("", share_method),
]