from django.urls import path, include
from main import views

app_name = 'start'
urlpatterns = [
    path('start_page/', views.start, name='start_page'),
    path('authorise/', views.authorise, name='authorise'),
    #path('hunter/', views.account_hunter, name='hunter'),
    #path('huntsman/', views.account_huntsman, name='huntsman'),
]