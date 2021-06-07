from BL_objects.price_list import *

from . import *
from .sector_rules import SectorRules
from .huntinggrounds_rules import HuntingGroundsRules
from inject_config import *


class PriceListRules(BaseRules):
    def get_sorted(self, list):
        return sorted(list, key=lambda x: (x['ground_name'], x['id_sector'],
                                           x['animal'], x['price']))

    def get_all(self):
        pricelist_rep = inject.instance(PriceListRepository)(self.connection)
        pricelist = pricelist_rep.get_all()

        res = []
        for elem in pricelist:
            elem = self.get_info(elem)
            res.append(elem)

        res = self.get_sorted(res)

        return res


    def get_info(self, pos: PriceList) -> dict:
        if pos is None:
            return None

        pos = pos.get_dict()

        sector = SectorRules('', self.connection).get_id_husbandry(pos['id_sector'])
        pos['id_husbandry'] = sector['id_husbandry']

        ground = HuntingGroundsRules('', self.connection).get_by_id(sector['id_husbandry'])
        pos['ground_name'] = ground['ground_name']

        return pos

    def get_by_id(self, id) -> PriceList:
        pricelist_rep = inject.instance(PriceListRepository)(self.connection)
        return pricelist_rep.get_by_id(id).get_dict()

    def get_by_login(self, login) -> dict:
        huntsmen_rep = inject.instance(HuntsmanRepository)(self.connection)
        pricelist_rep = inject.instance(PriceListRepository)(self.connection)

        huntsman = huntsmen_rep.get_by_login(login)
        price_set = pricelist_rep.get_by_sector(huntsman.get_id())

        if price_set is None:
            return None

        return price_set

    def get_by_sector(self, id_sector):
        pricelist_rep = inject.instance(PriceListRepository)(self.connection)
        price_set = pricelist_rep.get_by_sector(id_sector)

        if price_set is None:
            return None

        for i in range(len(price_set)):
            price_set[i] = price_set[i].get_dict()

        return price_set






