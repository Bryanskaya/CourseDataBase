from BL_objects.vouchers import *

from BL_rules.base_rules import *
from BL_rules.pricelist_rules import *
from BL_rules.hunter_rules import *
from errors.err_voucher import *


class VoucherRules(BaseRules):
    def create(self, data):
        obj = self.build_obj(data)

        vouchers_set = inject.instance(VoucherRepository)(self.connection)
        voucher = Voucher(obj)
        try:
            vouchers_set.create(voucher)
        except CreateBLObjectVoucherErr:
            voucher = None

        return voucher

    def build_obj(self, data):
        list_rules = PriceListRules('', connection=self.connection)

        if data['num'] == 0:
            raise WrongNumAnimals()

        obj = list_rules.get_by_id(data['id'])

        obj['amount_animals'] = data['num']
        obj['price'] = obj['price'] * data['num']

        hunter_rules = HunterRules('', connection=self.connection)
        hunter = hunter_rules.get_by_login(data['login']).get_dict()

        obj['id_hunter'] = hunter['ticket_num']
        obj['id_pricelist'] = obj['id']
        del obj['id']
        obj['status'] = False

        return obj

    def get_sorted(self, data):
        return sorted(data, key=lambda x: (x['ground_name'], x['id_sector'],
                                           x['animal'], x['amount_animals']))

    def get_by_login(self, login):
        hunter_rules = HunterRules('', connection=self.connection)
        vouchers_set = inject.instance(VoucherRepository)(self.connection)

        hunter = hunter_rules.get_by_login(login).get_dict()
        vouchers = vouchers_set.get_by_id_hunter(hunter['ticket_num'])

        res_true = []
        res_false = []
        for voucher in vouchers:
            temp = self.build_info(voucher)
            if temp['status']:
                res_true.append(temp)
            else:
                res_false.append(temp)

        res_true = self.get_sorted(res_true)
        res_false = self.get_sorted(res_false)

        return res_true, res_false

    def build_info(self, data: Voucher):
        list_rules = PriceListRules('', connection=self.connection)
        sector_rules = SectorRules('', connection=self.connection)
        ground_rules = HuntingGroundsRules('', connection=self.connection)

        data = data.get_dict()
        item = list_rules.get_by_id(data['id_pricelist'])

        data['animal'] = item['animal']
        data['id_sector'] = item['id_sector']

        sector = sector_rules.get_id_husbandry(data['id_sector'])
        ground = ground_rules.get_by_id(sector['id_husbandry'])

        data['ground_name'] = ground['ground_name']

        return data


