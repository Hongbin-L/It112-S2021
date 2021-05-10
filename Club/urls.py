from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getResource', views.getResource, name='getResource'),
]
