from django.shortcuts import render

from fit.models import Fit
from utils.response import *


# Create your views here.
def get_fit_list(request):
    if request.method == "GET":
        fit_list = Fit.objects.all()
        fit_list = list(fit_list.values())
        return success_response(fit_list)
    return fail_response()
