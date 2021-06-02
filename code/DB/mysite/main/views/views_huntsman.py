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


def contacts(request):
    huntsman_rules = HuntsmanRules(request.session['user']['role_eng'])
    huntsmen = huntsman_rules.get_all_detailed()

    return render(request, 'static/contacts.html', locals())