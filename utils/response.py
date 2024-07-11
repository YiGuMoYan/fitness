from django.http import JsonResponse


def success_response(data=None):
    success_res = {
        "code": 200,
        "message": "success",
        "data": data
    }
    return JsonResponse(success_res)


def fail_response(data=None):
    fail_res = {
        "code": 400,
        "message": "fail",
        "data": data
    }
    return JsonResponse(fail_res)
