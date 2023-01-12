from django.shortcuts import render
from django.http import HttpResponse
from featured.models import *


def create_featured(request):
    if request.method == 'GET':
        return render(request, 'featured/create_featured.html', context={})

    elif request.method == 'POST':
        Featured.objects.create(
            name = request.POST['name'],
            category = request.POST['category'],
        )
        return render(request, 'featured/create_featured.html', context={})

def list_featured(request):
    if 'search' in request.GET:
        search = request.GET['search']
        featured = Featured.objects.filter(name__contains=search)
    else:
        featured = Featured.objects.all()
    context = {
        'featured':featured,
    }
    return render(request, 'featured/list_featured.html', context=context)