from django.http import JsonResponse, HttpResponse
from .models import User
import json

def create_google_user(request):
    return JsonResponse(['a'], safe=False)

def get_user(request):
    b = User.objects.get(pk=2)
    return JsonResponse(b.backend_data(), safe=False)


def login(request):
    """
       Logins an user
       If the user is not yet created it creates it first and then does the login.
       :param request:
       :return:
    """
    data = dict(request.POST)
    u = User()
    if data['type'][0] == 'google':
        user_data = {
            'token': data['user_token'][0],
            'id': data['user_id'][0],
            'name': data['user_name'][0],
            'image_url': data['user_image_url'][0],
            'email': data['user_email'][0]
        }
        payload = u.google_validate(token=user_data['token'])
        if payload:
            return JsonResponse(u.create_google_user(payload=payload, user_data=user_data), safe=False)
        else:
            return HttpResponse('Unauthorized', status=401)

    return HttpResponse('Unauthorized', status=401)
