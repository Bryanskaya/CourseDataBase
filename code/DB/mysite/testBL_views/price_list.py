from BL_rules.pricelist_rules import *
from .base import *

class PriceListView(BaseView):
    @classmethod
    def get_all(cls):
        list_rules = PriceListRules('admin')
        offers = list_rules.get_all()
        return cls.set_to_str(offers)