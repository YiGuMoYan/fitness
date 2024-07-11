from django.shortcuts import render

from gym_location.models import GymLocation
from utils.response import *


# Create your views here.
def get_gym_list(request):
    if request.method == "GET":
        province = request.GET["province"]
        city = request.GET["city"]

        if province == "全部":
            gym_list = GymLocation.objects.values()
        elif city == "全部":
            gym_list = GymLocation.objects.filter(province=province).values()
        else:
            gym_list = GymLocation.objects.filter(province=province, city=city).values()
        gym_list = list(gym_list)

        return success_response(gym_list)
    return fail_response()


def get_province(request):
    if request.method == "GET":
        provinces = GymLocation.objects.values_list('province', flat=True).distinct()
        provinces = list(provinces)
        return success_response(provinces)
    return fail_response()


def get_city(request):
    if request.method == "GET":
        province = request.GET["province"]
        cities = GymLocation.objects.filter(province=province).values_list('city', flat=True).distinct()
        cities = list(cities)
        return success_response(cities)
    return fail_response()
