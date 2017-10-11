from django.shortcuts import render
from django.http import HttpResponse

import re

from .models import Email


def add(request):
    if request.method != 'POST':
        return HttpResponse(status=500)

    email = request.POST.get("email", "")
    if not Email.objects.filter(address=email).exists():
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return HttpResponse(status=400)
        else:
            n = Email()
            n.address = email
            n.save()
            return HttpResponse(status=200)
    else:
        return HttpResponse(status=409)