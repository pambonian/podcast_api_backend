from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='rss-home'), 
    path('feed/', views.rss, name='rss-feed'), 
]