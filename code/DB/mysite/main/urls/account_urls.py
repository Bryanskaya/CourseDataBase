from django.urls import path, include
from main.views import views

from logging_act import *

app_name = 'start'
urlpatterns = [
    path('start_page/', lambda req, **kwargs: do_log(views.start, req, **kwargs), name='start_page'),
    path('exit_from/', lambda req, **kwargs: do_log(views.exit_from, req, **kwargs), name='exit_from'),
    path('register_page/', views.register_form, name='register_form'),
    path('register/', lambda req, **kwargs: do_log(views.register, req, proved=False, **kwargs), name='register'),
    path('authorise/', views.authorise, name='authorise'),
    path('register_page/get_sectors/', views.get_sectors, name='get_sectors'),
    path('recover_password/<str:login>', views.recover_password, name='recover_password'),
    path('check_code/', views.check_code, name='check_code'),
    path('log_requests/', views.requests_to_log, name='requests'),
    path('show_admins/', views.show_admins, name='show_admins'),
    path('find/', lambda req, **kwargs: do_log(views.find, req, **kwargs), name='find'),

]