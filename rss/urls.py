from django.urls import path
from .import views 

urlpatterns = [
    
    path('', views.home, name='rss-home'), 
    path('/site_home', views.home, name='site_home'), 
     
]