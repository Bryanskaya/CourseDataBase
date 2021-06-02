from django.urls import path, include
from main.views import views_hunter

app_name = 'hunters'
urlpatterns = [
    path('buy/', views_hunter.buy, name='buy'),
    path('buy/<int:id>&<int:num>', views_hunter.request_voucher, name='request_voucher'),
    path('show/', views_hunter.show_cur_vouchers, name='show'),
    path('show/<int:id>', views_hunter.del_request, name='del_request'),

]