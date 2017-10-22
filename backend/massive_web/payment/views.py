from django.http import JsonResponse


def new(request, id):
    return JsonResponse({'a': 4}, safe=False)
