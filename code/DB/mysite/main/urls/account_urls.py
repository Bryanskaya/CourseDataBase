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
    path('register_page/get_sectors/', lambda req, **kwargs: do_log(views.get_sectors, req, **kwargs), name='get_sectors'),
    path('recover_password/<str:login>', views.recover_password, name='recover_password'),
    path('check_code/', views.check_code, name='check_code'),
    path('log_requests/', views.requests_to_log, name='requests'),
    path('show_admins/', views.show_admins, name='show_admins'),
    path('find/', lambda req, **kwargs: do_log(views.find, req, **kwargs), name='find'),
    path('requests_admins/', lambda req, **kwargs: do_log(views.show_req_admins, req, **kwargs), name='show_req_admins'),
    path('requests_all/', lambda req, **kwargs: do_log(views.show_req_hunters, req, **kwargs), name='show_req_hunters'),
    path('requests_huntsmen/', lambda req, **kwargs: do_log(views.show_req_huntsmen, req, **kwargs), name='show_req_huntsmen'),
    path('accept_reg/<str:login>', lambda req, **kwargs: do_log(views.accept_reg_admins, req, **kwargs), name='accept_reg_admins'),
    path('accept_reg_htn/<str:login>', lambda req, **kwargs: do_log(views.accept_reg_hunters, req, **kwargs), name='accept_reg_hunters'),
    path('accept_reg_htns/<str:login>', lambda req, **kwargs: do_log(views.accept_reg_huntsmen, req, **kwargs), name='accept_reg_huntsmen'),
    path('reject_reg/<str:login>', lambda req, **kwargs: do_log(views.reject_reg_admins, req, **kwargs), name='reject_reg_admins'),
    path('reject_reg_hnt/<str:login>', lambda req, **kwargs: do_log(views.reject_reg_hunters, req, **kwargs), name='reject_reg_hunters'),
    path('reject_reg_hnts/<str:login>', lambda req, **kwargs: do_log(views.reject_reg_huntsmen, req, **kwargs), name='reject_reg_huntsmen'),
    path('reject_acc/<str:login>', lambda req, **kwargs: do_log(views.reject_acc_admins, req, **kwargs), name='reject_acc_admins'),

]