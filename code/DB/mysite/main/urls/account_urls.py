from django.urls import path, include
from main import views

app_name = 'start'
urlpatterns = [
    path('start_page/', views.start, name='start_page'),
    path('exit_from/', views.exit_from, name='exit_from'),
    path('register_page/', views.register_form, name='register_form'),
    path('register/', views.register, name='register'),
    path('authorise/', views.authorise, name='authorise'),
    path('register_page/get_sectors/', views.get_sectors, name='get_sectors'),
    #path('recover_password/', views.recover_password, name='recover_password'),
    #path('hunter/', views.account_hunter, name='hunter'),
    #path('huntsman/', views.account_huntsman, name='huntsman'),
]