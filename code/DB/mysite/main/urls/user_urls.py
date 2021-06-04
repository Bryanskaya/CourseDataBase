from django.urls import path
from main.views import views

from logging_act import *

app_name = 'users'
urlpatterns = [
    path('about/', lambda req, **kwargs: do_log(views.about, req, **kwargs), name='about'),
    path('about/<str:login>', lambda req, **kwargs: do_log(views.account, req, **kwargs), name='account'),
]