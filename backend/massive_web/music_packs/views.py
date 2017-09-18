from django.http import JsonResponse
from django.conf import settings
from .models import MusicPack

import random

BASE_IMG_PATH = settings.BASE_URL + "src/img/"
BASE_AUDIO_PATH = settings.BASE_URL + "src/audio/"

# Create your views here.
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
    titles = ["Four loko", "Fixie nostrud", "Master Cleanse", "Scenester hell", "Shabby chic", "Blue bottle",
               "Duis pitchfork", "Raclette portland", "Cardigan glossier", "Tumeric keffiyeh"]
    descriptions = [
        "<p>That's a popular name today. Eeeee! Now say \"nuclear wessels\"! It doesn't look so shiny to me. Good news, everyone! I've taught the toaster to feel love! Switzerland is small and neutral! We are more like Germany, ambitious and misunderstood!The key to victory is discipline, and that means a well made bed. You will practice until you can make your bed in your sleep. </p> <p>For the last time, I don't like lilacs! Your 'first' wife was the one who liked lilacs! </p>",
        "<p>Hodor, hodor hodor; hodor hodor - hodor, hodor. Hodor hodor hodor! Hodor hodor - hodor - hodor. Hodor hodor HODOR! Hodor hodor; hodor hodor?! Hodor hodor HODOR! Hodor hodor... Hodor hodor hodor. Hodor hodor HODOR! Hodor hodor, hodor. Hodor hodor - hodor. Hodor. </p><p>Hodor, hodor. Hodor. Hodor, hodor hodor hodor... Hodor hodor HODOR hodor, hodor hodor. Hodor, hodor hodor? Hodor, hodor; hodor hodor hodor?! Hodor, hodor. Hodor. Hodor, hodor hodor hodor hodor! Hodor, hodor - hodor... Hodor hodor hodor?! </p>",
        "<p>Who are you, my warranty?! You'll have all the Slurm you can drink when you're partying with Slurms McKenzie! Can we have Bender Burgers again? Is that a cooking show?</p><p>Son, as your lawyer, I declare y'all are in a 12-piece bucket o' trouble. But I done struck you a deal: Five hours of community service cleanin' up that ol' mess you caused. These old Doomsday Devices are dangerously unstable. I'll rest easier not knowing where they are.</p>",
        "<p>Oh right. I forgot about the battle. Soothe us with sweet lies. Yeah, I do that with my stupidness. Morbo can't understand his teleprompter because he forgot how you say that letter that's shaped like a man wearing a hat.</p><p>Stop! Don't shoot fire stick in space canoe! Cause explosive decompression! You won't have time for sleeping, soldier, not with all the bed making you'll be doing. I love you, buddy! That's not soon enough!</p>"
    ]
    authors = ["Philip J. Fry", "Turanga Leela", "Bender Bending Rodriguez", "Doctor John Zoidberg", "Lord Nibbler"]
    songs = [
        {"id": 1, "name": "Happy Birthday Variation: In the style of Beethoven", "lenght": "2:30", "file": BASE_AUDIO_PATH + "001.mp3"},
        {"id": 2, "name": "Wedding March Variation 1", "lenght": "1:30", "file": BASE_AUDIO_PATH + "002.mp3"},
        {"id": 3, "name": "Happy Birthday Variation: In the style of Tango", "lenght": "1:33", "file": BASE_AUDIO_PATH + "003.mp3"},
        {"id": 4, "name": "Wedding March Variation 2", "lenght": "3:20", "file": BASE_AUDIO_PATH + "004.mp3"},
        {"id": 5, "name": "Random Classical", "lenght": "1:12", "file": BASE_AUDIO_PATH + "005.mp3"},
        {"id": 6, "name": "Everything is true", "lenght": "0:22", "file": BASE_AUDIO_PATH + "006.mp3"},
        {"id": 7, "name": "Cuicuitte ", "lenght": "12:00", "file": BASE_AUDIO_PATH + "007.mp3"},
        {"id": 8, "name": "J'aurai toujours peur de me perdre", "lenght": "2:32", "file": BASE_AUDIO_PATH + "008.mp3"}
    ]
    categories = ['RPG', 'Action', 'FPS', 'Puzzle']

    return JsonResponse({
            'id': int(id),
            'img' : BASE_IMG_PATH + '00' + str(random.randint(1, 8)) +'.jpg',
            'title': random.choice(titles),
            'price': float(random.randint(1000, 8000) / 100),
            'author': random.choice(authors),
            'description': random.choice(descriptions),
            'tracks': [random.choice(songs) for _ in range(random.randint(1, 5))],
            'categories': [random.choice(categories) for _ in range(random.randint(1,2))]
        }, safe=False)
