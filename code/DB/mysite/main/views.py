from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import sys

sys.path.append("../")

from BL_rules.account_rules import *


def prove_account(request, controller: BaseAccountCheck):
    if 'user' not in request.session.keys():
        return HttpResponseRedirect(reverse('start:start_page'))

    try:
        controller.check(request.session['user'])
    except:
        return HttpResponseRedirect(reverse('start:start_page'))

    return None


def start(request):
    if prove_account(request, AllRolesCheck()):
        return render(request, 'static/start_page.html')
    return HttpResponseRedirect(reverse('users:about'))


def exit_from(request):
    if 'user' in request.session:
        del request.session['user']
    return HttpResponseRedirect(reverse('start:start_page'))


def authorise(request):
    account = AccountRules.is_log_in(request.POST['username'], request.POST['password'])
    if account is not None:
        request.session['user'] = AccountRules.get_cookie(account)
        return HttpResponseRedirect(reverse('users:about'))
    else:
        return render(request, 'static/start_page.html', {
            'error_message': 'Неверный логин/пароль',
        })


def about(request):
    check = prove_account(request, AllRolesCheck())
    if check:
        return check

    account = AccountRules.get_person(request.session['user']['login'])
    return render(request, 'static/about.html', locals())


def account(request, login):
    test = prove_account(request, AllRolesCheck())
    if test:
        return test

    if login == request.session['user']['login']:
        return HttpResponseRedirect(reverse('users:about'))

    account = AccountRules.get_person(login)
    return render(request, 'static/about.html', locals())