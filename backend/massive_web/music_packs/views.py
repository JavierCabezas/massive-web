from django.http import JsonResponse
from .models import MusicPack


def music_packs(request):
    mps = MusicPack.objects.all()
    return JsonResponse([mp.backend() for mp in mps], safe=False)


def music_pack(request, id):
    mp = MusicPack.objects.get(id=id)
    return JsonResponse(mp.backend_detail(), safe=False)