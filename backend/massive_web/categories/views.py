from django.shortcuts import render
from django.http import JsonResponse
from .models import Category

def parents(request):
    '''
    Returns an json array with all the categories on the first level
    :param request:
    :return:
    '''
    cats = Category.objects.filter(level=1)
    return JsonResponse([c.backend() for c in cats], safe=False)