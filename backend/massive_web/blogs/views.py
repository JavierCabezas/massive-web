from django.http import JsonResponse

from .models import Blog

import random

def posts(request):
    return JsonResponse([b.backend() for b in Blog.objects.all()], safe=False)

def post(request, id):
    b = Blog.objects.get(id=id)
    return JsonResponse(b.backend(), safe=False)
