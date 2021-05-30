from django.urls import path, include
from main.views import views

app_name = 'users'
urlpatterns = [
    path('about/', views.about, name='about'),
    path('about/<str:login>', views.account, name='account'),
    #path('huntsman/', views.account_huntsman, name='huntsman'),
]