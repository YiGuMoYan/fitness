import datetime
import json
from urllib.parse import parse_qs

from django.shortcuts import render

from training_log.models import TrainingLog
from utils.response import *


# Create your views here.
def training_log_method(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        date = datetime.datetime.strptime(request.POST.get("date"), '%Y-%m-%d')

        # 获取前端传递的数据
        data_string = request.body.decode('utf-8')  # 解码请求体
        parsed_data = parse_qs(data_string)

        # 解析嵌套的数据结构
        data = []
        for key, value in parsed_data.items():
            if key.startswith('data['):
                index = key.split('[')[1].split(']')[0]  # 提取索引号
                if index.isdigit():  # 确保是有效的索引
                    index = int(index)
                    if index >= len(data):
                        data.append({})
                    subkey = key.split(']')[1].strip('[')  # 提取子键名
                    data[index][subkey] = value[0]  # 将值存入对应的子字典中

        # 处理每个数据项并创建 TrainingLog 对象
        for item in data:
            duration = float(item["duration"])
            content = item["content"]
            sets = int(item["sets"])
            reps = int(item["reps"])
            weight = float(item["weight"])

            # 创建 TrainingLog 对象并保存
            TrainingLog.objects.create(
                user_id=user_id,
                date=date,
                duration=duration,
                content=content,
                sets=sets,
                reps=reps,
                weight=weight
            )

        return success_response()
    return fail_response()


def training_log_list(request):
    if request.method == "GET":
        user_id = request.GET["user_id"]
        logs = TrainingLog.objects.filter(user_id=user_id).values()
        logs = list(logs)
        time_list = [log["date"].strftime('%Y-%m-%d') for log in logs]
        res = []
        for time in time_list:
            if time in [item["date"] for item in res]:
                continue
            log_list = [log for log in logs if log["date"].strftime('%Y-%m-%d') == time]
            res.append({
                "date": time,
                "logs": log_list
            })
        return success_response(res)
    return fail_response()


def training_log_delete(request):
    if request.method == "POST":
        date = request.POST.get("date")
        user_id = request.POST.get("user_id")
        TrainingLog.objects.filter(user_id=user_id, date=date).delete()
        return success_response()
    return fail_response()
