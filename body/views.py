import datetime

from body.models import Body
from utils.response import *


# Create your views here.
def body_method(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        record_date = datetime.datetime.strptime(request.POST["record_date"], '%Y-%m-%d')
        height = request.POST["height"]
        weight = request.POST["weight"]

        Body.objects.create(user_id=user_id, record_date=record_date, height=height, weight=weight)
        return success_response()

    if request.method == "GET":
        id = request.GET["id"]
        user_id = request.GET["user_id"]
        body = Body.objects.filter(id=id, user_id=user_id).first()
        if body is None:
            return fail_response("记录不存在")
        return success_response(body)

    return fail_response()


def update(request):
    if request.method == "POST":
        id = request.POST["id"]
        user_id = request.POST["user_id"]
        body = Body.objects.filter(id=id, user_id=user_id).first()
        if body is None:
            return fail_response("记录不存在")
        body.record_date = datetime.datetime.strptime(request.POST["record_date"], '%Y-%m-%d')
        body.height = request.POST["height"]
        body.weight = request.POST["weight"]
        body.save()
        return success_response()


def delete(request):
    if request.method == "GET":
        id = request.GET["id"]
        user_id = request.GET["user_id"]
        body = Body.objects.filter(id=id, user_id=user_id).first()
        if body is None:
            return fail_response("记录不存在")
        body.delete()
        return success_response()


def get_list(request):
    if request.method == "GET":
        user_id = request.GET["user_id"]
        body_list = Body.objects.filter(user_id=user_id).order_by("record_date").values()
        body_list = list(body_list)
        for diet in body_list:
            diet["record_date"] = diet["record_date"].strftime('%Y-%m-%d')
        return success_response(body_list)
    return fail_response()
