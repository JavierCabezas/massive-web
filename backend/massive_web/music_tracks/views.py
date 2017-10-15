from django.http import JsonResponse
from .models import MusicTrack
from ..categories.models import Category


def music_tracks(request):
    if 'category_id' in request.GET and int(request.GET['category_id']) > 0:
        cat = Category.objects.get(id=int(request.GET['category_id']))
        mts = MusicTrack.objects.filter(category_id__in=cat.family())
    else:
        mts = MusicTrack.objects.all()

    return JsonResponse([mt.backend() for mt in mts], safe=False)


def music_track(request, id):
    mt = MusicTrack.objects.get(id=id)
    return JsonResponse(mt.backend(True), safe=False)
