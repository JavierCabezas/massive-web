from django.http import JsonResponse
from django.conf import settings
from .models import MusicPack

def music_packs(request):
    out = []
    for p in MusicPack.objects.all():
        out.append({
            'id': p.id,
            'img': settings.BASE_URL + p.image.name,
            'title': p.name,
            'text': p.short_description,
            'price': p.price
        })
    return JsonResponse(out, safe=False)

def music_pack(request, id):
    p = MusicPack.objects.get(id=id)

    return JsonResponse({
            'id': p.id,
            'img' : settings.BASE_URL + p.image.name,
            'title': p.name,
            'price': p.price,
            'author': "TO-DO",
            'short_description': p.short_description,
            'long_description': p.long_description,
            'tracks': [song.backend() for song in p.music_tracks.all()],
            'category': p.category.name
        }, safe=False)
