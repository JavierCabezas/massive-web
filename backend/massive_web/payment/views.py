from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from datetime import datetime

from .models import Cart
from ..users.models import User
from ..music_packs.models import MusicPack
from ..music_tracks.models import MusicTrack

from paypal.standard.forms import PayPalPaymentsForm


def create_cart(request):
    if not request.method == 'POST':
        return HttpResponse(status=405)

    music_pack_ids = list(int(x) for x in request.POST.getlist('music_packs[]'))
    music_tracks_ids = list(int(x) for x in request.POST.getlist('music_tracks[]'))
    token = request.POST['user_token']
    user = User.get_user_by_token(token=token)
    if user is None:
        return HttpResponse(status=401)

    music_packs_objs = MusicPack.objects.filter(id__in=music_pack_ids)
    music_tracks_ojbs = MusicTrack.objects.filter(id__in=music_tracks_ids)

    c = Cart()
    c.creation_date = datetime.now()
    c.payment_date = None
    c.deleted_date = None
    c.calculate_amount(music_packs_objs, music_tracks_ojbs)
    c.user_id = user.id
    c.save()

    if len(music_packs_objs) > 0:
        c.music_packs.add(*music_packs_objs)
    if len(music_tracks_ojbs) > 0:
        c.music_tracks.add(*music_tracks_ojbs)

    return JsonResponse(c.id, safe=False)


def new(request, id):
    pp = PayPalPaymentsForm

    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return_url": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)


def confirm():
    return True