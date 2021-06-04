from django.urls import path, include
from main.views import views_huntsman

from logging_act import *

app_name = 'huntsmen'
urlpatterns = [
    path('contacts/', lambda req, **kwargs: do_log(views_huntsman.contacts, req, **kwargs), name='contacts'),
]