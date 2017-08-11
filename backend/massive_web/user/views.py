from django.http import JsonResponse
from .models import  User

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
    type = request.POST.type
    user_data = request.POST.user_data

    if type == 'google':
        google_response = 'a'

#    return JsonResponse(out, safe=False)
