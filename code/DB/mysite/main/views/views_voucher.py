from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

import sys

from read_data import *

sys.path.append("../")

from BL_rules.account_rules import *
from BL_rules.hunter_rules import *
from BL_rules.huntsman_rules import *
from BL_rules.sector_rules import *
from BL_rules.pricelist_rules import *
from BL_rules.voucher_rules import *


def requests(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    requests = voucher_rules.get_requests_by_login(request.session['user']['login'])

    return render(request, 'static/requests.html', locals())

def requests_all(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    requests = voucher_rules.get_requests_all()

    return render(request, 'static/requests_all.html', locals())


def accept(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    voucher_rules.accept(id)
    requests = voucher_rules.get_requests_by_login(request.session['user']['login'])

    return render(request, 'static/requests.html', locals())

def accept_by_admin(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    voucher_rules.accept(id)
    requests = voucher_rules.get_requests_all()

    return render(request, 'static/requests_all.html', locals())

def reject(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])

    voucher_rules.delete(id)
    requests = voucher_rules.get_vouchers(request.session['user']['login'])

    return render(request, 'static/requests.html', locals())

def reject_by_admin(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])

    voucher_rules.delete(id)
    requests = voucher_rules.get_requests_all()

    return render(request, 'static/requests_all.html', locals())

def huntsman_vouchers(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    vouchers = voucher_rules.get_vouchers(request.session['user']['login'])
    return render(request, 'static/vouchers.html', locals())

def create_voucher(request):
    pricelist_rules = PriceListRules(request.session['user']['role_eng'])
    offers = pricelist_rules.get_by_login(request.session['user']['login'])

    return render(request, 'static/new_voucher.html', locals())

def create_by_huntsman(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    pricelist_rules = PriceListRules(request.session['user']['role_eng'])

    offers = pricelist_rules.get_by_login(request.session['user']['login'])

    try:
        voucher = voucher_rules.create_by_params(request.POST)
    except TicketHunterNotExists:
        error_message = "Охотника с таким билетом нет в базе"
        return render(request, 'static/new_voucher.html', locals())

    return HttpResponseRedirect(reverse('vouchers:huntsman_vouchers'))

def create_by_admin(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    pricelist_rules = PriceListRules(request.session['user']['role_eng'])
    huntsmen_rules = HuntsmanRules(request.session['user']['role_eng'])

    offers = pricelist_rules.get_all()
    hunting_grounds = csv_dict_reader()

    return render(request, 'static/add_voucher_admin.html', locals())

def add_by_admin(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    pricelist_rules = PriceListRules(request.session['user']['role_eng'])

    offers = pricelist_rules.get_all
    hunting_grounds = csv_dict_reader()

    print("***** ", request.POST)

    '''self.id = data['id']
        self.amount_animals = data['amount_animals']
        self.price = data['price']
        self.id_hunter = data['id_hunter']
        self.id_pricelist = data['id_pricelist']
        self.status = data['status']'''

    try:
        voucher = voucher_rules.create_by_params(request.POST)
    except TicketHunterNotExists:
        error_message = "Охотника с таким билетом нет в базе"
        return render(request, 'static/add_voucher_admin.html', locals())

    return HttpResponseRedirect(reverse('users:about'))

def get_cur_vouchers(request):
    pricelist_rules = PriceListRules(request.session['user']['role_eng'])

    if request.is_ajax and request.method == "POST":
        pricelist_set = pricelist_rules.get_by_sector(request.POST['id_sector'])
        return JsonResponse({'pricelist': pricelist_set}, status=200)
    return JsonResponse({}, status=200)


