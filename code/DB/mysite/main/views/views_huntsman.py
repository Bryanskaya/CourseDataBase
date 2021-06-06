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

from read_data import *

def contacts(request):
    huntsman_rules = HuntsmanRules(request.session['user']['role_eng'])
    huntsmen = huntsman_rules.get_all_detailed()

    return render(request, 'static/contacts.html', locals())

def show_huntsmen(request):
    huntsmen_rules = HuntsmanRules(request.session['user']['role_eng'])
    huntsmen = huntsmen_rules.get_all_detailed()
    huntsmen = get_acc(huntsmen)
    hunting_grounds = csv_dict_reader()

    return render(request, 'static/show_huntsmen.html', locals())

def get_acc(huntsmen: [dict]):
    i = 0
    while i < len(huntsmen):
        if huntsmen[i]['type_role'] != 'егерь':
            huntsmen.pop(i)
            continue
        i += 1

    return huntsmen


def find(request):
    huntsmen_rules = HuntsmanRules(request.session['user']['role_eng'])

    data = {}
    data['surname'] = request.POST['surname']
    data['name'] = request.POST['firstname']
    data['patronymic'] = request.POST['patronymic']
    if 'id_husbandry' in request.POST.keys():
        data['id_husbandry'] = int(request.POST['id_husbandry'])
    else:
        data['id_husbandry'] = ''
    huntsmen = huntsmen_rules.get_by_params(data)
    hunting_grounds = csv_dict_reader()

    return render(request, 'static/show_huntsmen.html', locals())

def reject_reg(request, login):
    account_rules = AccountRules(request.session['user']['role_eng'])
    account_rules.reject_huntsman(login)

    return HttpResponseRedirect(reverse('huntsmen:show_huntsmen'))