from django.shortcuts import render
from django.http import HttpResponse
# from django.views.decorators.http import require_GET

from .models import Articles

# @require_GET
def index(request):
    return render(request, 'index.html')


def listArts(request):
    data = Articles.objects.all()[0: 10]
    print(data)
    return render(request, 'listArts.html', {'result': data})


def art(request):
    data = Articles.objects.get(pk=1)
    print(data)
    return render(request, 'art.html', {'result': data})

def test(request, html):
    return HttpResponse(html)
