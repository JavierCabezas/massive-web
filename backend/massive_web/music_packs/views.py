from django.http import JsonResponse
from .models import MusicPack
from ..categories.models import Category

def music_packs(request):
    if 'category_id' in request.GET and int(request.GET['category_id']) > 0:
        cat = Category.objects.get(id=int(request.GET['category_id']))
        mps = MusicPack.objects.filter(category_id__in=cat.family())
    else:
        mps = MusicPack.objects.all()
    return JsonResponse([mp.backend() for mp in mps], safe=False)


def music_pack(request, id):
    mp = MusicPack.objects.get(id=id)
    return JsonResponse(mp.backend_detail(), safe=False)