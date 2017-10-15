from django.http import JsonResponse

from .models import Blog


def posts(request, limit=None):
    if limit is None:
        return JsonResponse([b.backend() for b in Blog.objects.all()], safe=False)
    else:
        return JsonResponse([b.backend() for b in Blog.objects.all()[:int(limit)]], safe=False)


def post(request, id):
    b = Blog.objects.get(id=id)
    return JsonResponse(b.backend(), safe=False)
