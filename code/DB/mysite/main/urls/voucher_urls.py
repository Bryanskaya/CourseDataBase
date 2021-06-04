from django.urls import path
from main.views import views_voucher

from logging_act import *

app_name = 'vouchers'
urlpatterns = [
    path('requests/', lambda req, **kwargs: do_log(views_voucher.requests, req, **kwargs), name='requests'),
    path('requests/reject/<int:id>', lambda req, **kwargs: do_log(views_voucher.reject, req, **kwargs), name='reject'),
    path('requests/accept/<int:id>', lambda req, **kwargs: do_log(views_voucher.accept, req, **kwargs), name='accept'),
    path('vouchers/', lambda req, **kwargs: do_log(views_voucher.huntsman_vouchers, req, **kwargs), name='huntsman_vouchers'),
    path('new_voucher/', lambda req, **kwargs: do_log(views_voucher.create_voucher, req, **kwargs), name='create_voucher'),
    path('add_voucher/', lambda req, **kwargs: do_log(views_voucher.create_by_huntsman, req, **kwargs), name='create_by_huntsman'),
]