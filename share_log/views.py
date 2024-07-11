import os
import uuid

from account.models import Account
from comment.models import Comment
from fitness.settings import MEDIA_ROOT
from share_log.models import Share
from utils.response import *


# Create your views here.
def upload(request):
    if request.method == "POST":
        try:
            file = request.FILES.get("file")
            # 获取图片昵称
            file_name = file.name
            # 获取图片后缀
            file_extend = file_name.split(".")[-1]
            # 判断图片格式
            if file_extend.lower() not in ["jpg", "jpeg", "png", "pdf"]:
                return fail_response("图片格式错误")
            file_name = f"{uuid.uuid4().hex}.{file_extend}"
            # 保存图片
            file_path = os.path.join(MEDIA_ROOT, file_name)
            with open(file_path, "wb") as f:
                for chunk in file.chunks():
                    f.write(chunk)
            return success_response(data={"image_name": file_name})
        except Exception as e:
            return fail_response(str(e))
    return fail_response("上传失败")


def share_method(request):
    if request.method == "POST":
        user_id = request.POST["user_id"]
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.POST["image"]
        Share.objects.create(user_id=user_id, title=title, content=content, image=image)
        return success_response()
    if request.method == "GET":
        id = request.GET["id"]
        share = Share.objects.filter(id=id).first()
        if share is None:
            return fail_response("无权限")
        res = {
            "id": share.id,
            "title": share.title,
            "content": share.content,
            "image": share.image,
            "create_time": share.create_time.strftime("%Y-%m-%d %H:%M:%S")
        }
        return success_response(data=res)
    return fail_response()


def get_list(request):
    if request.method == "GET":
        user_id = request.GET["user_id"]
        shares = Share.objects.filter(user_id=user_id).values()
        shares = list(shares)
        for share in shares:
            share["create_time"] = share["create_time"].strftime("%Y-%m-%d %H:%M:%S")
        return success_response(data=shares)
    return fail_response()


def delete(request):
    if request.method == "GET":
        id = request.GET["id"]
        user_id = request.GET["user_id"]
        share = Share.objects.filter(id=id, user_id=user_id).values()
        if share is None:
            return fail_response("无权限")
        Share.objects.filter(id=id).delete()
        Comment.objects.filter(share_id=id).delete()
        return success_response()
    return fail_response()


def update(request):
    if request.method == "POST":
        id = request.POST["id"]
        user_id = request.POST["user_id"]
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.POST["image"]
        share = Share.objects.filter(id=id, user_id=user_id).values()
        if share is None:
            return fail_response("无权限")
        Share.objects.filter(id=id).update(title=title, content=content, image=image)
        return success_response()
    return fail_response()


def get_view_list(request):
    if request.method == "GET":
        shares = Share.objects.values()
        shares = list(shares)
        for share in shares:
            share["create_time"] = share["create_time"].strftime("%Y-%m-%d %H:%M:%S")
            share["name"] = Account.objects.get(id=share["user_id"]).username
        return success_response(data=shares)
    return fail_response()