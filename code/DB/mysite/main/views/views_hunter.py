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


def buy(request):
    voucher_rules = PriceListRules(request.session['user']['role_eng'])
    offers = voucher_rules.get_all()

    return render(request, 'static/buy.html', locals())