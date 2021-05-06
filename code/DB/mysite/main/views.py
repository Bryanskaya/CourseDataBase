from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *

import sys

sys.path.append("../")

from inject_config import *
from BL_rules.account_rules import *


def home(request):
    # data = Accounts.objects.filter(login__exact='GorNa_03_08_1988')

    # data = get_hunters_by_id_sct(10)
    # return render(request, 'static/index.html', {'title': 'Пробуем вывести', 'info': {'test1': 1, 'test2': 22}})

    if request.method == 'POST':
        print(request.POST)

    return render(request, 'static/start_page.html')
    # return render(request, 'static/start_hunter.html')
    # return render(request, 'static/start_huntsman.html')
    # return render(request, 'static/map.html')

    '''
    proc_add_voucher(10, 21, 0, 26703800, 1)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''
    proc_delete_voucher(1208)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''
    proc_mark_point_pricelist_irrelevant('чирок', 89)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''
    proc_add_point_pricelist('чирок', 870, 89)
    return render(request, 'main\index.html', {'title': 'Пробуем вывести'})
    '''

    '''if request.method == 'POST':
        error = ''
        form = UserForm(request.POST)
        print(form)

        if form.is_valid():
            #form.save()
            return redirect('index')
        else:
            error = 'Неверные данные'

    form = UserForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main\index.html', context)'''


def authorise(request):
    if request.method == 'POST':
        print(request.POST)

    account = AccountRules.is_log_in(request.POST['username'], request.POST['password'])
    if account:
        role = account.get_type_role()
        if role == 'охотник':
            #return render(request, '/static/start_hunter.html')
            return HttpResponseRedirect(reverse('start:hunter'))
        elif role == 'егерь':
            return render(request, '/static/start_huntsman.html')
        elif role == 'админ':
            return HttpResponse('Я - админ')  # TODO страница для админа
    else:
        # return HttpResponseRedirect(reverse('start:start_page', kwargs={
        #     'error_message': 'Неверный логин/пароль'
        # }))
        return render(request, 'static/start_page.html', {
            'error_message': 'Неверный логин/пароль',
        })

def account_hunter(request):
    return render(request, 'static/start_hunter.html')