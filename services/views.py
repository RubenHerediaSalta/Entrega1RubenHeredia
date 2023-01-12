from django.shortcuts import render
from django.http import HttpResponse
from services.models import *


def create_services(request):
    if request.method == 'GET':
        return render(request, 'services/create_services.html', context={})

    elif request.method == 'POST':
        Services.objects.create(
            name = request.POST['name'],
            description = request.POST['description'],
            price = request.POST['price'],
        )
        return render(request, 'services/create_services.html', context={})

def list_services(request):
    if 'search' in request.GET:
        search = request.GET['search']
        services = Services.objects.filter(name__contains=search)
    else:
        services = Services.objects.all()
    context = {
        'services':services,
    }
    return render(request, 'services/list_services.html', context=context)