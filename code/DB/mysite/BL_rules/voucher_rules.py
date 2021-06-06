from BL_objects.vouchers import *

from BL_rules.base_rules import *
from BL_rules.pricelist_rules import *
from BL_rules.hunter_rules import *
from BL_rules.account_rules import *
from pattern_repository.detailed_voucher import *
from errors.err_voucher import *
from errors.err_general import *
from errors.err_hunter import *


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

    def create_by_params(self, data):
        data = self.to_dict(data)
        hunter_rules = HunterRules('', connection=self.connection)
        vouchers_set = inject.instance(VoucherRepository)(self.connection)

        hunter = hunter_rules.get_by_ticket_num(data['ticket_num'])

        if hunter is None:
            raise TicketHunterNotExists()

        data['id_hunter'] = data['ticket_num']
        data['status'] = True

        voucher = Voucher(data)
        try:
            vouchers_set.create(voucher)
        except CreateBLObjectVoucherErr:
            voucher = None

        return voucher


    def accept(self, id):
        vouchers_set = inject.instance(VoucherRepository)(self.connection)
        vouchers_set.accept(id)


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

    def delete(self, id):
        vouchers_set = inject.instance(VoucherRepository)(self.connection)
        try:
            vouchers_set.delete_by_id(id)
        except:
            raise DeleteVoucherErr()

    def delete_by_huntsman(self, id_hunter):
        vouchers_set = inject.instance(VoucherRepository)(self.connection)
        try:
            vouchers_set.delete_by_huntsman(id_hunter)
        except:
            raise DeleteVoucherErr()


    def get_sorted(self, data):
        return sorted(data, key=lambda x: (x['ground_name'], x['id_sector'],
                                           x['animal'], x['amount_animals']))

    def get_by_login(self, login):
        hunter_rules = HunterRules('', connection=self.connection)
        vouchers_set = inject.instance(VoucherRepository)(self.connection)

        try:
            hunter = hunter_rules.get_by_login(login).get_dict()
        except:
            raise LoginNotExists()

        vouchers = vouchers_set.get_by_id_hunter(hunter['ticket_num'])

        if vouchers is None:
            return vouchers, None

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

    def get_requests_by_login(self, login):
        huntsmen_set = inject.instance(HuntsmanRepository)(self.connection)
        vouchers_set = inject.instance(VoucherRepository)(self.connection)

        huntsman = huntsmen_set.get_by_login(login).get_dict()
        id_sector = huntsman['id']

        requests = vouchers_set.get_requests(id_sector)

        if requests is None:
            return None

        for i in range(len(requests)):
            requests[i] = self.build_request(requests[i])

        return sorted(requests, key=lambda x: (x['surname'], x['name'],
                                               x['patronymic'], x['id_voucher'],
                                               x['animal']))

    def get_vouchers(self, login):
        huntsmen_set = inject.instance(HuntsmanRepository)(self.connection)
        vouchers_set = inject.instance(VoucherRepository)(self.connection)

        try:
            huntsman = huntsmen_set.get_by_login(login).get_dict()
        except:
            return None

        id_sector = huntsman['id']

        requests = vouchers_set.get_vouchers(id_sector)

        if requests is None:
            return None

        for i in range(len(requests)):
            requests[i] = self.build_request(requests[i])

        return sorted(requests, key=lambda x: (x['surname'], x['name'],
                                               x['patronymic'], x['id_voucher'],
                                               x['animal']))

    def get_vouchers_all(self):
        vouchers_set = inject.instance(DetailedVoucherRepository)(self.connection)
        vouchers = vouchers_set.get_vouchers_all()

        for i in range(len(vouchers)):
            temp = vouchers[i].get_dict()
            temp['full_name'] = temp['surname'] + ' ' + temp['firstname'] + ' ' + temp['patronymic']
            vouchers[i] = temp

        return sorted(vouchers, key=lambda x: (x['surname'], x['firstname'],
                                               x['patronymic'], x['id_voucher'],
                                               x['animal']))

    def build_request(self, data: Voucher):
        hunter_rules = HunterRules('', connection=self.connection)
        list_rules = PriceListRules('', connection=self.connection)
        account_rules = AccountRules('', connection=self.connection)

        data = data.get_dict()
        data['id_voucher'] = data['id']

        hunter = hunter_rules.get_by_ticket_num(data['id_hunter']).get_dict()
        account = account_rules.get_person(hunter['login']).get_dict()

        data['surname'] = account['surname']
        data['name'] = account['firstname']
        data['patronymic'] = account['patronymic']
        data['full_name'] = data['surname'] + ' ' + data['name'] + \
            ' ' + data['patronymic']
        data['mobile_phone'] = account['mobile_phone']
        data['email'] = account['email']

        item = list_rules.get_by_id(data['id_pricelist'])
        data['animal'] = item['animal']

        return data

    def get_requests_all(self):
        vouchers_set = inject.instance(DetailedVoucherRepository)(self.connection)
        vouchers = vouchers_set.get_requests_all()

        for i in range(len(vouchers)):
            temp = vouchers[i].get_dict()
            temp['full_name'] = temp['surname'] + ' ' + temp['firstname'] + ' ' + temp['patronymic']
            vouchers[i] = temp
        return vouchers


