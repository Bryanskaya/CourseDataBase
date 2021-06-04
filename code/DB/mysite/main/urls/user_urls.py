from django.urls import path, include
from main.views import views

from logging_act import *

app_name = 'users'
urlpatterns = [
    path('about/', lambda req, **kwargs: do_log(views.about, req, **kwargs), name='about'),
    path('about/<str:login>', views.account, name='account'),
    #path('huntsman/', views.account_huntsman, name='huntsman'),
]