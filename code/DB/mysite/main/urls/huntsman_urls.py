from django.urls import path, include
from main.views import views_huntsman

app_name = 'huntsmen'
urlpatterns = [
    path('contacts/', views_huntsman.contacts, name='contacts'),
]