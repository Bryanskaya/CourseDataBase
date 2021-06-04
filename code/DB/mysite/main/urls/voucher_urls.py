from django.urls import path, include
from main.views import views_voucher

app_name = 'vouchers'
urlpatterns = [
    path('requests/', views_voucher.requests, name='requests'),
    path('requests/reject/<int:id>', views_voucher.reject, name='reject'),
    path('requests/accept/<int:id>', views_voucher.accept, name='accept'),
    path('vouchers/', views_voucher.huntsman_vouchers, name='huntsman_vouchers'),
    path('new_voucher/', views_voucher.create_voucher, name='create_voucher'),
]