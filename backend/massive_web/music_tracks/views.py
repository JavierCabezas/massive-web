from django.utils.encoding import smart_str
from django.http import JsonResponse
from django.http import HttpResponse

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


def download_private_track(request, id):
    mt = MusicTrack.objects.get(id=id)
    response = HttpResponse(content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(mt.downloaded_file_name())
    response['X-Sendfile'] = smart_str(mt.song.url)
    return response

