from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from datetime import datetime, date
import sys

sys.path.append("../")

from BL_rules.account_rules import *
from BL_rules.hunter_rules import *


def prove_account(request, controller: BaseAccountCheck):
    if 'user' not in request.session.keys():
        return HttpResponseRedirect(reverse('start:start_page'))

    try:
        controller.check(request.session['user'])
    except:
        return render(request, 'static/start_page.html', {
            'error_message': 'Ваша заявка рассматривается',
        })

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
    print("/// views ", check)
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


def register_form(request):
    roles = AccountRules.get_roles()
    return render(request, 'static/register_page.html', locals())


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def register(request):
    data = dict(request.POST.copy())
    print(data)

    roles = AccountRules.get_roles()

    for key in data.keys():
        data[key] = data[key][0]

    try:
        datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()
    except:
        data['error_message'] = 'Неверно введена дата рождения'
        return render(request, 'static/register_page.html', locals())

    if calculate_age(datetime.strptime(data['date_of_birth'], '%Y-%m-%d').date()) < 18:
        data['date_of_birth'] = ''
        data['error_message'] = 'Минимально допустимый возраст - 18 лет'
        return render(request, 'static/register_page.html', locals())

    if data['password'] != data['repeated_password']:
        data['repeated_password'] = ''
        data['error_message'] = 'Пароли не совпадают'
        return render(request, 'static/register_page.html', locals())

    data['info_message'] = 'Ваша заявка отправлена'

    account = AccountRules.register(data['login'], data['password'],
                                    data['surname'], data['firstname'],
                                    data['patronymic'], data['date_of_birth'],
                                    data['sex'], data['phone'],
                                    data['email'], data['role'])

    if account is None:
        data['error_message'] = 'Текущий логин уже используется'
        data['login'] = ''
        return render(request, 'static/register_page.html', locals())

    cur_role = AccountRules.get_role_eng(account.get_type_role()[1:])
    if cur_role == 'hunter':
        hunter = Hunter(data)
        hunter = HunterRules.register(hunter)

        if hunter is None:
            AccountRules.delete_account(account)
            data['error_message'] = 'Ошибка регистрации данных'
            return render(request, 'static/register_page.html', locals()) # TODO надо ли сохранять введенные данные
    elif cur_role == 'huntsman':
        huntsman = Huntsman(data)




    elif cur_role == 'admin':
        pass

    return render(request, 'static/start_page.html', locals())