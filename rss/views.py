from django.shortcuts import render
from django.http import HttpResponse
from .rss_info import items


def home(request):
    context = {
        'items': items
    }
    print('Items', type(items))
    return render(request, 'rss/home.html', context)






