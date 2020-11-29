from django.contrib import admin
from django.urls import path
from .views import index #Relativ import av viewsfunksjonen

appname = "elsysapp"
urlpatterns = [
    path('', index, name='index'),
]

from django.conf import settings
from django.contrib.staticfiles import views
from django.urls import re_path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

if settings.DEBUG:
   urlpatterns += staticfiles_urlpatterns()