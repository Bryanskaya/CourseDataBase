from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

import sys

sys.path.append("../")

from BL_rules.account_rules import *
from BL_rules.hunter_rules import *
from BL_rules.huntsman_rules import *
from BL_rules.sector_rules import *
from BL_rules.pricelist_rules import *
from BL_rules.voucher_rules import *


def buy(request):
    voucher_rules = PriceListRules(request.session['user']['role_eng'])
    offers = voucher_rules.get_all()

    return render(request, 'static/buy.html', locals())

def request_voucher(request, id, num):
    list_rules = PriceListRules(request.session['user']['role_eng'])
    voucher_rules = VoucherRules(request.session['user']['role_eng'])

    offers = list_rules.get_all()
    try:
        voucher = voucher_rules.create({'id': id, 'num': num, 'login': request.session['user']['login']})
    except WrongNumAnimals:
        error_message = 'Введите количество'
        return render(request, 'static/buy.html', locals())

    if voucher is None:
        error_message = 'Возникли проблемы с отправкой заявки'
        return render(request, 'static/buy.html', locals())

    info_message = 'Заявка на путёвку отправлена'

    return render(request, 'static/buy.html', locals())


def show_cur_vouchers(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])

    try:
        vouchers, requests = voucher_rules.get_by_login(request.session['user']['login'])
    except LoginNotExists:
        vouchers, requests = [], []
        error_message = 'Ошибка логина'

    return render(request, 'static/show.html', locals())


def del_request(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])

    try:
        voucher_rules.delete(id)
    except DeleteVoucherErr:
        error_message = 'Не удалось выполнить действие'
        return render(request, 'static/show.html', locals())

    vouchers, requests = voucher_rules.get_by_login(request.session['user']['login'])
    info_message = 'Заявка успешно отозвана'

    return render(request, 'static/show.html', locals())


def show_all(request):
    return HttpResponseRedirect(reverse('hunters:all'))


def find_all(request):
    hunters_rules = HunterRules(request.session['user']['role_eng'])
    #hunters = hunters_rules.get_all_detailed()
    hunters = hunters_rules.get_acc_hunters()

    return render(request, 'static/all.html', locals())


def find(request):
    hunters_rules = HunterRules(request.session['user']['role_eng'])

    data = {}
    data['surname'] = request.POST['surname']
    data['name'] = request.POST['firstname']
    data['patronymic'] = request.POST['patronymic']
    data['ticket_num'] = request.POST['ticket_num']
    hunters = hunters_rules.get_by_params(data)

    return render(request, 'static/all.html', locals())


def reject_reg(request, login):
    account_rules = AccountRules(request.session['user']['role_eng'])
    account_rules.reject_hunter(login)

    return HttpResponseRedirect(reverse('hunters:show_all'))

