from django.shortcuts import render
from django.http import HttpResponse
from categories.models import *


def create_categories(request):
    if request.method == 'GET':
        return render(request, 'categories/create_categories.html', context={})

    elif request.method == 'POST':
        Categories.objects.create(
            name = request.POST['name'],
        )
        return render(request, 'categories/create_categories.html', context={})

def list_categories(request):
    if 'search' in request.GET:
        search = request.GET['search']
        categories = Categories.objects.filter(name__contains=search)
    else:
        categories = Categories.objects.all()
    context = {
        'categories':categories,
    }
    return render(request, 'categories/list_categories.html', context=context)