from django.urls import path
from .import views 



urlpatterns = [
    path('', views.home, name='rss-home'),
    path('videos/', views.videos, name='rss-videos'),
]