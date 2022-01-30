from django.shortcuts import render
from .rss_info import item_results
# from .sandbox_3 import data


def home(request):
    context = {
        'items': item_results
    }
    
    return render(request, 'rss/home.html', context)

# def booking(request):
#     return render(request, 'rss/booking.html')


# def videos(request):
#     return render( )




