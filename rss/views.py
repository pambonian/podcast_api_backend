from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        # put rss info here. 
    }
    return render(request, 'blog/home.html', context)

def videos(request):
    return HttpResponse('<h1>Rss Videos</>')


