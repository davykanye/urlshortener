from django.urls import path

from . import views
from .api import endpoints

app_name = 'shortener'
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', endpoints.Index, name='api_setURL'),
    path('<slug:slug>/', views.rerouter, name='shorturl'),
]