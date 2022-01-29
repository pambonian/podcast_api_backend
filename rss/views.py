from django.shortcuts import render
from .rss_info import items


def home(request):
    context = {
        'items': items
    }
    print('Items', items)
    return render(request, 'rss/home.html', context)


# def videos(request):
#     return render( )




