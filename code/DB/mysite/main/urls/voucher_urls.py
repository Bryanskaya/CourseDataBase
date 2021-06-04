from django.urls import path, include
from main.views import views_voucher

app_name = 'vouchers'
urlpatterns = [
    path('requests/', views_voucher.show_requests, name='show_requests'),
]