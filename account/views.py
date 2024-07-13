from account.models import Account
from utils.crypt import decrypt
from utils.response import *


def login(request):
    if request.method == "POST":
        data = decrypt(request.body)
        email = data["email"]
        password = data["password"]
        if not Account.objects.filter(email=email).exists():
            return fail_response("用户名不存在")
        account = Account.objects.filter(email=email).first()
        if password == account.password:
            return success_response({"user_id": account.id})
        return fail_response("密码错误")
    return fail_response()


def signup(request):
    if request.method == "POST":
        data = decrypt(request.body)
        username = data["username"]
        password = data["password"]
        email = data["email"]
        if Account.objects.filter(username=username).exists():
            return fail_response("用户名已存在")
        account = Account.objects.create(username=username, password=password, email=email)
        return success_response({"user_id": account.id})
    return fail_response()


def account_method(request):
    if request.method == "GET":
        user_id = request.GET["user_id"]
        account = Account.objects.filter(id=user_id).values().first()
        if account is None:
            return fail_response("用户不存在")
        res = {
            "user_id": account["id"],
            "username": account["username"],
            "email": account["email"]
        }
        return success_response(res)
    if request.method == "POST":
        data = decrypt(request.body)
        user_id = data["user_id"]
        username = data["username"]
        email = data["email"]
        account = Account.objects.filter(id=user_id).first()
        if account is None:
            return fail_response("用户不存在")
        account.username = username
        account.email = email
        account.save()
        return success_response()
    return fail_response()


def update_password(request):
    if request.method == "POST":
        data = decrypt(request.body)
        user_id = data["user_id"]
        old_password = data["old_password"]
        new_password = data["new_password"]
        account = Account.objects.filter(id=user_id).first()
        if account is None:
            return fail_response("用户不存在")
        if old_password != account.password:
            return fail_response("密码错误")
        account.password = new_password
        account.save()
        return success_response()
    return fail_response()
