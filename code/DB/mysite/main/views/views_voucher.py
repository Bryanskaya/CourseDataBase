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


def requests(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    requests = voucher_rules.get_requests_by_login(request.session['user']['login'])

    return render(request, 'static/requests.html', locals())

def accept(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    voucher_rules.accept(id)
    requests = voucher_rules.get_requests_by_login(request.session['user']['login'])

    return render(request, 'static/requests.html', locals())

def reject(request, id):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    voucher_rules.delete(id)
    requests = voucher_rules.get_requests_by_login(request.session['user']['login'])

    return render(request, 'static/requests.html', locals())

def huntsman_vouchers(request):
    voucher_rules = VoucherRules(request.session['user']['role_eng'])
    vouchers = voucher_rules.get_vouchers(request.session['user']['login'])
    return render(request, 'static/vouchers.html', locals())

def create_voucher(request):
    pricelist_rules = PriceListRules(request.session['user']['role_eng'])
    offers = pricelist_rules.get_by_login(request.session['user']['login'])

    return render(request, 'static/new_voucher.html', locals())
