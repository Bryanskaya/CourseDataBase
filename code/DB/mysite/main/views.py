from django.shortcuts import render
# from .models import Accounts
from .models import *


def home(request):
    #data = Accounts.objects.filter(login__exact='GorNa_03_08_1988')
    data = get_vouchers_by_id_sct(55)
    #print("+++++", data)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести', 'info': data})