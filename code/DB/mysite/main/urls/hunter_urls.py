from django.urls import path, include
from main.views import views_hunter

from logging_act import *

app_name = 'hunters'
urlpatterns = [
    path('buy/', lambda req, **kwargs: do_log(views_hunter.buy, req, **kwargs), name='buy'),
    path('buy/<int:id>&<int:num>', lambda req, **kwargs: do_log(views_hunter.request_voucher, req, **kwargs), name='request_voucher'),
    path('show/', lambda req, **kwargs: do_log(views_hunter.show_cur_vouchers, req, **kwargs), name='show'),
    path('show/<int:id>', lambda req, **kwargs: do_log(views_hunter.del_request, req, **kwargs), name='del_request'),
    path('all/', lambda req, **kwargs: do_log(views_hunter.find_all, req, **kwargs), name='show_all'),
    path('find/', lambda req, **kwargs: do_log(views_hunter.find, req, **kwargs), name='find'),
    path('reject_reg/<str:login>', lambda req, **kwargs: do_log(views_hunter.reject_reg, req, **kwargs), name='reject_reg'),

]