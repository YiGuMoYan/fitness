from django.shortcuts import render

from food.models import Food
from utils.response import success_response


# Create your views here.
def food_list(request):
    food = Food.objects.values_list('name', flat=True).distinct()
    food = list(food)
    return success_response({"food": food})
