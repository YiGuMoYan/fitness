import datetime

from django.shortcuts import render

from diet.models import Diet
from food.models import Food
from utils.response import *


# Create your views here.
def diet_method(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        record_date = datetime.datetime.strptime(request.POST["record_date"], '%Y-%m-%d')
        breakfast = request.POST["breakfast"]
        breakfast_weight = float(request.POST["breakfast_weight"])
        lunch = request.POST["lunch"]
        lunch_weight = float(request.POST["lunch_weight"])
        dinner = request.POST["dinner"]
        dinner_weight = float(request.POST["dinner_weight"])
        note = request.POST["note"]

        breakfast_heat = Food.objects.filter(name=breakfast).first().heat * breakfast_weight
        lunch_heat = Food.objects.filter(name=lunch).first().heat * lunch_weight
        dinner_heat = Food.objects.filter(name=dinner).first().heat * dinner_weight

        sum_heat = breakfast_heat + lunch_heat + dinner_heat
        Diet.objects.create(user_id=user_id, record_date=record_date, breakfast=breakfast, breakfast_weight=breakfast_weight,
                            breakfast_heat=breakfast_heat, lunch=lunch, lunch_weight=lunch_weight, lunch_heat=lunch_heat,
                            dinner=dinner, dinner_weight=dinner_weight, dinner_heat=dinner_heat, note=note,
                            sum=sum_heat)

        return success_response()

    if request.method == "GET":
        id = request.GET["id"]
        user_id = request.GET["user_id"]
        diet = Diet.objects.filter(id=id, user_id=user_id).first()
        if diet is None:
            return fail_response("记录不存在")
        return success_response(diet)

    return fail_response()


def update(request):
    if request.method == "POST":
        id = request.POST["id"]
        user_id = request.POST["user_id"]
        diet = Diet.objects.filter(id=id, user_id=user_id).first()
        if diet is None:
            return fail_response("记录不存在")
        diet.record_date = datetime.datetime.strptime(request.POST["record_date"], '%Y-%m-%d')
        diet.breakfast = request.POST["breakfast"]
        diet.breakfast_weight = float(request.POST["breakfast_weight"])
        diet.lunch = request.POST["lunch"]
        diet.lunch_weight = float(request.POST["lunch_weight"])
        diet.dinner = request.POST["dinner"]
        diet.dinner_weight = float(request.POST["dinner_weight"])
        diet.note = request.POST["note"]

        diet.breakfast_heat = Food.objects.filter(name=diet.breakfast).first().heat * diet.breakfast_weight
        diet.lunch_heat = Food.objects.filter(name=diet.lunch).first().heat * diet.lunch_weight
        diet.dinner_heat = Food.objects.filter(name=diet.dinner).first().heat * diet.dinner_weight
        diet.sum = diet.breakfast_heat + diet.lunch_heat + diet.dinner_heat

        diet.save()
        return success_response()


def delete(request):
    if request.method == "GET":
        id = request.GET["id"]
        user_id = request.GET["user_id"]
        diet = Diet.objects.filter(id=id, user_id=user_id).first()
        if diet is None:
            return fail_response("记录不存在")
        diet.delete()
        return success_response()


def get_list(request):
    if request.method == "GET":
        user_id = request.GET["user_id"]
        diet_list = Diet.objects.filter(user_id=user_id).order_by("record_date").values()
        diet_list = list(diet_list)
        for diet in diet_list:
            diet["record_date"] = diet["record_date"].strftime('%Y-%m-%d')
        return success_response(diet_list)
    return fail_response()
