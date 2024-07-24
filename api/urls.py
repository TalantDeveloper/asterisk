from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('info/', views.asterisk_info, name='info'),
    path('variable/', views.asterisk_variable, name='variable'),
    path('bridges/', views.bridges, name='bridges'),
    path('channels/', views.channels, name='channels'),
    path('states/', views.device_states, name='states'),
    path('endpoints/', views.endpoints, name='endpoints'),
    path('events/', views.events, name='events'),
    path('mailboxes/', views.mailboxes, name='mailboxes'),
    path('stored/', views.recordings_stored, name='stored'),
    path('sounds/', views.sounds, name='sounds'),
]