from account.models import Account
from comment.models import Comment
from utils.crypt import decrypt
from utils.response import *


# Create your views here.
def get_comment(request):
    if request.method == "GET":
        share_id = request.GET["share_id"]
        comments = Comment.objects.filter(share_id=share_id).order_by("-create_time").values()
        comments = list(comments)
        res = []
        for comment in comments:
            data = {
                "id": comment["id"],
                "user_id": comment["user_id"],
                "content": comment["content"],
                "create_time": comment["create_time"].strftime("%Y-%m-%d %H:%M:%S"),
                "username": Account.objects.get(id=comment["user_id"]).username
            }
            res.append(data)
        return success_response(data=res)
    return fail_response()


def add_comment(request):
    if request.method == "POST":
        data = decrypt(request.body)
        user_id = data["user_id"]
        share_id = data["share_id"]
        content = data["content"]
        Comment.objects.create(user_id=user_id, share_id=share_id, content=content)
        return success_response()
    return fail_response()