from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getResource', views.getResource, name='getResource'),
    path('getMeeting', views.getMeeting, name='getMeeting'),
    path('meetingDetail/<int:id>', views.meetingDetails, name='meetingDetails'),
    path('newResource', views.newResource, name='newResource'),
    path('newMeeting', views.newMeeting, name='newMeeting'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]
