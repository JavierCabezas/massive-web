from django.http import JsonResponse
from .models import  User

def create_google_user(request):
    return JsonResponse(['a'], safe=False)

def get_user(request):
    b = User.objects.get(pk=2)
    return JsonResponse(b.backend_data(), safe=False)