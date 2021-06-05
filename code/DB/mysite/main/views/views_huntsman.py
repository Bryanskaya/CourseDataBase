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
    hunting_grounds = csv_dict_reader()

    return render(request, 'static/show_huntsmen.html', locals())


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