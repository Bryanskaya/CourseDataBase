from django.urls import path
from main.views import views_voucher

from logging_act import *

app_name = 'vouchers'
urlpatterns = [
    path('requests/', lambda req, **kwargs: do_log(views_voucher.requests, req, **kwargs), name='requests'),
    path('requests/reject/<int:id>', lambda req, **kwargs: do_log(views_voucher.reject, req, **kwargs), name='reject'),
    path('delete_voucher/<int:id>', lambda req, **kwargs: do_log(views_voucher.delete_voucher, req, **kwargs), name='delete_voucher'),
    path('requests/reject_by_admin/<int:id>', lambda req, **kwargs: do_log(views_voucher.reject_by_admin, req, **kwargs), name='reject_by_admin'),
    path('requests/rejectv_by_admin/<int:id>', lambda req, **kwargs: do_log(views_voucher.rejectv_by_admin, req, **kwargs), name='rejectv_by_admin'),
    path('requests/accept/<int:id>', lambda req, **kwargs: do_log(views_voucher.accept, req, **kwargs), name='accept'),
    path('requests/accept_by_admin/<int:id>', lambda req, **kwargs: do_log(views_voucher.accept_by_admin, req, **kwargs), name='accept_by_admin'),
    path('vouchers/', lambda req, **kwargs: do_log(views_voucher.huntsman_vouchers, req, **kwargs), name='huntsman_vouchers'),
    path('vouchers_admin/', lambda req, **kwargs: do_log(views_voucher.admin_vouchers, req, **kwargs), name='admin_vouchers'),
    path('new_voucher/', lambda req, **kwargs: do_log(views_voucher.create_voucher, req, **kwargs), name='create_voucher'),
    path('add_voucher/', lambda req, **kwargs: do_log(views_voucher.create_by_huntsman, req, **kwargs), name='create_by_huntsman'),
    path('add_voucher_admin/', lambda req, **kwargs: do_log(views_voucher.create_by_admin, req, **kwargs), name='create_by_admin'),
    path('add_voucher_admint/', lambda req, **kwargs: do_log(views_voucher.add_by_admin, req, **kwargs), name='add_by_admin'),
    path('all_vouchers/admin', lambda req, **kwargs: do_log(views_voucher.requests_all, req, **kwargs), name='requests_all'),
    path('get_cur_vouchers/', lambda req, **kwargs: do_log(views_voucher.get_cur_vouchers, req, **kwargs), name='get_cur_vouchers'),
]