from BL_objects.price_list import *

from BL_rules.base_rules import *
from BL_rules.sector_rules import *
from BL_rules.huntinggrounds_rules import *


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




