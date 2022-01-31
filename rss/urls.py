from django.urls import path
from .import views 

urlpatterns = [
    path('', views.home, name='rss-home'), 
    
    # path('booking/', views.booking, name='booking'), 
]