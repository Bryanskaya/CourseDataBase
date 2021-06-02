from inject_config import *
from BL_objects.huntsman import *
from errors.err_huntsman import *
from BL_rules.base_rules import *


class HuntsmanRules(BaseRules):
    def register(self, obj: Huntsman):
        huntsman_set = inject.instance(HuntsmanRepository)(self.connection)
        try:
            huntsman_set.create(obj)
        except CreateBLObjectHuntsmanErr:
            obj = None

        return obj

    def get_by_login(self, login):
        huntsman_set = inject.instance(HuntsmanRepository)(self.connection)
        return huntsman_set.get_by_login(login)

    def get_all(self):
        huntsman_set = inject.instance(HuntsmanRepository)(self.connection)
        huntsmen = huntsman_set.get_all()

        for i in range(len(huntsmen)):
            huntsmen[i] = huntsmen[i].get_dict()

        return huntsmen

    def get_all_detailed(self):
        huntsman_set = inject.instance(HuntsmanRepository)(self.connection)
        huntsmen = huntsman_set.get_all()

        for i in range(len(huntsmen)):
            pers = huntsmen[i].get_dict()

            accounts_set = inject.instance(AccountsRepository)(self.connection)
            account = accounts_set.get_by_login(pers['login']).get_dict()

            pers['id_sector'] = pers['id']
            del pers['id']
            pers['full_name'] = account['surname'] + ' ' + account['firstname'] + \
                ' ' + account['patronymic']
            pers['mobile_phone'] = account['mobile_phone']
            pers['email'] = account['email']

            sectors_set = inject.instance(SectorsRepository)(self.connection)
            sector = sectors_set.get_by_id(pers['id_sector']).get_dict()

            grounds_set = inject.instance(HuntingGroundsRepository)(self.connection)
            ground = grounds_set.get_by_id(sector['id_husbandry']).get_dict()

            pers['ground_name'] = ground['ground_name']

            huntsmen[i] = pers

        return huntsmen



