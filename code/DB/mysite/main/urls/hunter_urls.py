from django.urls import path, include
from main.views import views_hunter

app_name = 'hunters'
urlpatterns = [
    path('buy/', views_hunter.buy, name='buy'),
]