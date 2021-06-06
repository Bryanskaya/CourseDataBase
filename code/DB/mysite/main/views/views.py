from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse

from datetime import datetime, date
import sys

sys.path.append("../")

from BL_rules.account_rules import *
from BL_rules.hunter_rules import *
from BL_rules.huntsman_rules import *
from BL_rules.sector_rules import *
from BL_rules.huntinggrounds_rules import *

from read_data import *


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
    acc_rules = AccountRules('admin')
    account = acc_rules.is_log_in(request.POST['username'], request.POST['password'])
    if account is not None:
        request.session['user'] = acc_rules.get_cookie(account)
        return HttpResponseRedirect(reverse('users:about'))
    else:
        return render(request, 'static/start_page.html', {
            'error_message': 'Неверный логин/пароль',
        })


def add_info(request, account: Account):
    account = account.get_dict()
    acc_rules = AccountRules(request.session['user']['role_eng'])

    role = acc_rules.get_role_eng(account['type_role'])
    login = account['login']

    if role == 'hunter':
        hunter_rules = HunterRules(request.session['user']['role_eng'])

        hunter = hunter_rules.get_by_login(login).get_dict()
        account['residence'] = hunter['residence']
        account['ticket_num'] = hunter['ticket_num']
    elif role == 'huntsman' or role == 'егерь':
        huntsmen_rules = HuntsmanRules(request.session['user']['role_eng'])
        sectors_rules = SectorRules(request.session['user']['role_eng'])
        grounds_rules = HuntingGroundsRules(request.session['user']['role_eng'])

        huntsman = huntsmen_rules.get_by_login(login).get_dict()
        sector = sectors_rules.get_by_id(huntsman['id']).get_dict()
        ground = grounds_rules.get_by_id(sector['id_husbandry'])

        account['id_sector'] = huntsman['id']
        account['ground_name'] = ground['ground_name']

    return account

def about(request):
    check = prove_account(request, AllRolesCheck())
    if check:
        return check

    acc_rules = AccountRules(request.session['user']['role_eng'])
    account = acc_rules.get_person(request.session['user']['login'])
    account = add_info(request, account)

    return render(request, 'static/about.html', locals())


def account(request, login):
    test = prove_account(request, AllRolesCheck())
    if test:
        return test

    if login == request.session['user']['login']:
        return HttpResponseRedirect(reverse('users:about'))

    acc_rules = AccountRules(request.session['user']['role_eng'])
    account = acc_rules.get_person(login)
    return render(request, 'static/about.html', locals())


def register_form(request):
    acc_rules = AccountRules('admin')
    roles = acc_rules.get_roles()
    hunting_grounds = csv_dict_reader()
    return render(request, 'static/register_page.html', locals())


def recover_password(request, login):
    acc_rules = AccountRules('admin')
    account = acc_rules.is_exist_login(login)

    if account is None:
        return render(request, 'static/recover_password.html', {
            'error_message': 'Указанного логина нет в системе',
        })

    if account.get_type_role() not in acc_rules.get_roles():
        return render(request, 'static/start_page.html', {
            'error_message': 'Ваша заявка рассматривается',
        })

    email = account.get_email()

    #TODO send email

    return render(request, 'static/recover_password.html', locals())


def check_code(request):
    cur_code = request.POST['num1'] + request.POST['num2'] + \
               request.POST['num3'] + request.POST['num4']
    #if cur_code == code:
    return render(request, 'static/new_password.html')
    #else
    # return render(request, 'static/recover_password.html', {
    #     'error_message': 'Неверный код',
    # })


def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def register(request, proved):
    data = dict(request.POST.copy())
    acc_rules = AccountRules('admin')
    roles = acc_rules.get_roles()
    hunting_grounds = csv_dict_reader()

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

    if (data['role'] == 'егерь' or data['role'] == 'huntsman') and ['sectors'] == 'null':
        data['hunting_grounds'] = ''
        data['sectors'] = ''
        data['error_message'] = 'Выбранный субъект не доступен, выберете другой'
        return render(request, 'static/register_page.html', locals())

    if data['password'] != data['repeated_password']:
        data['repeated_password'] = ''
        data['error_message'] = 'Пароли не совпадают'
        return render(request, 'static/register_page.html', locals())

    data['info_message'] = 'Ваша заявка отправлена'

    account = acc_rules.register(data['login'], data['password'],
                                    data['surname'], data['firstname'],
                                    data['patronymic'], data['date_of_birth'],
                                    data['sex'], data['phone'],
                                    data['email'], data['role'])

    if proved:
        account.set_type_role(data['role'][1:])

    if account is None:
        data['error_message'] = 'Текущий логин уже используется'
        data['login'] = ''
        return render(request, 'static/register_page.html', locals())

    cur_role = acc_rules.get_role_eng(account.get_type_role()[1:])
    user = 'delete_me'
    if cur_role == 'hunter':
        hunter_rules = HunterRules('admin')
        user = Hunter(data)
        user = hunter_rules.register(user)
    elif cur_role == 'huntsman':
        huntsman_rules = HuntsmanRules('admin')
        data['id'] = data['sectors']
        user = Huntsman(data)
        user = huntsman_rules.register(user)

    if user is None:
        acc_rules.delete_account(account)
        data['error_message'] = 'Ошибка регистрации данных'
        return render(request, 'static/register_page.html', locals())

    return render(request, 'static/start_page.html', locals())


def get_sectors(request):
    sect_rules = SectorRules('admin')
    if request.is_ajax and request.method == "POST":
        sectors_set = sect_rules.get_ids(request.POST['id'])
        return JsonResponse({'id': sectors_set}, status=200)
    return JsonResponse({}, status=200)

def requests_to_log(request):
    return render(request, 'static/log_requests.html', locals())

def show_admins(request):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    if 'error_message' in request.session.keys():
        error_message = request.session['error_message']
        del request.session['error_message']

    admins = acc_rules.get_acc_admins()

    for i in range(len(admins)):
        admins[i]['full_name'] = admins[i]['surname'] + ' ' + admins[i]['firstname'] + ' ' + \
                               admins[i]['patronymic']

    return render(request, 'static/show_admins.html', locals())

def find(request):
    acc_rules = AccountRules(request.session['user']['role_eng'])

    data = {}
    data['surname'] = request.POST['surname']
    data['name'] = request.POST['firstname']
    data['patronymic'] = request.POST['patronymic']

    admins = acc_rules.get_by_params(data)
    for i in range(len(admins)):
        admins[i]['full_name'] = admins[i]['surname'] + ' ' + admins[i]['firstname'] + ' ' + \
                               admins[i]['patronymic']

    return render(request, 'static/show_admins.html', locals())

def show_req_admins(request):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    admins = acc_rules.get_req_admins()

    for i in range(len(admins)):
        admins[i]['full_name'] = admins[i]['surname'] + ' ' + admins[i]['firstname'] + ' ' + \
                                 admins[i]['patronymic']

    return render(request, 'static/requests_admins.html', locals())

def show_req_hunters(request):
    hunters_rules = HunterRules(request.session['user']['role_eng'])
    requests = hunters_rules.get_req_hunters()

    for i in range(len(requests)):
        requests[i]['full_name'] = requests[i]['surname'] + ' ' + requests[i]['name'] + ' ' + \
                                 requests[i]['patronymic']

    return render(request, 'static/requests_all.html', locals())

def show_req_huntsmen(request):
    huntsmen_rules = HuntsmanRules(request.session['user']['role_eng'])
    requests = huntsmen_rules.get_req_huntsmen()

    for i in range(len(requests)):
        requests[i]['full_name'] = requests[i]['surname'] + ' ' + requests[i]['name'] + ' ' + \
                                   requests[i]['patronymic']

    return render(request, 'static/requests_huntsmen.html', locals())

def accept_reg_admins(request, login):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    acc_rules.accept(login)

    return HttpResponseRedirect(reverse('start:show_req_admins'))

def accept_reg_hunters(request, login):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    acc_rules.accept(login)

    return HttpResponseRedirect(reverse('start:show_req_hunters'))

def accept_reg_huntsmen(request, login):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    acc_rules.accept(login)

    return HttpResponseRedirect(reverse('start:show_req_huntsmen'))

def reject_reg_admins(request, login):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    if login == request.session['user']['login']:
        request.session['error_message'] = 'Отказано: попытка удалить свой аккаунт'
        return HttpResponseRedirect(reverse('start:show_admins'))

    acc_rules.reject_admin(login)

    return HttpResponseRedirect(reverse('start:show_req_admins'))

def reject_reg_hunters(request, login):
    account_rules = AccountRules(request.session['user']['role_eng'])
    account_rules.reject_hunter(login)

    return HttpResponseRedirect(reverse('start:show_req_hunters'))

def reject_reg_huntsmen(request, login):
    account_rules = AccountRules(request.session['user']['role_eng'])
    account_rules.reject_huntsman(login)

    return HttpResponseRedirect(reverse('start:show_req_huntsmen'))

def reject_acc_admins(request, login):
    acc_rules = AccountRules(request.session['user']['role_eng'])
    if login == request.session['user']['login']:
        request.session['error_message'] = 'Отказано: попытка удалить свой аккаунт'
        return HttpResponseRedirect(reverse('start:show_admins'))

    acc_rules.reject_admin(login)

    return HttpResponseRedirect(reverse('start:show_admins'))

