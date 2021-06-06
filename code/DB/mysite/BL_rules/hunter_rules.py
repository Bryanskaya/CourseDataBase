from inject_config import *
from BL_objects.hunter import *
from errors.err_hunter import *

from BL_rules.base_rules import *


class HunterRules(BaseRules):
    def get_sorted(self, arr: [Hunter]):
        return sorted(arr, key=lambda x: (x['surname'], x['name'],
                                           x['patronymic']))

    def register(self, obj: Hunter):
        hunters_set = inject.instance(HunterRepository)(self.connection)

        try:
            hunters_set.create(obj)
        except CreateBLObjectHunterErr:
            obj = None

        return obj

    def delete_by_huntsman(self, ticket_num):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        hunters_set.delete_by_huntsman(ticket_num)

    def get_by_login(self, login):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        return hunters_set.get_by_login(login)

    def get_by_ticket_num(self, num):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        return hunters_set.get_by_ticket_num(num)

    def get_all(self):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        hunters = hunters_set.get_all()

        for i in range(len(hunters)):
            hunters[i] = hunters[i].get_dict()

        hunters = self.get_sorted(hunters)

        return hunters

    def get_all_detailed(self):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        accounts_set = inject.instance(AccountsRepository)(self.connection)

        hunters = hunters_set.get_all()

        i = 0
        while i < len(hunters):
            pers = hunters[i].get_dict()
            account = accounts_set.get_by_login(pers['login']).get_dict()

            if account['type_role'] != 'охотник':
                hunters.pop(i)
                continue

            pers['full_name'] = account['surname'] + ' ' + account['firstname'] + \
                ' ' + account['patronymic']
            pers['surname'] = account['surname']
            pers['name'] = account['firstname']
            pers['patronymic'] = account['patronymic']
            pers['mobile_phone'] = account['mobile_phone']
            pers['email'] = account['email']
            pers['date_of_birth'] = account['date_of_birth']
            pers['type_role'] = account['type_role']

            hunters[i] = pers

            i += 1

        hunters = self.get_sorted(hunters)

        return hunters

    def get_req_hunters(self):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        accounts_set = inject.instance(AccountsRepository)(self.connection)

        hunters = hunters_set.get_all()

        i = 0
        while i < len(hunters):
            pers = hunters[i].get_dict()
            account = accounts_set.get_by_login(pers['login']).get_dict()

            if account['type_role'] != '#охотник':
                hunters.pop(i)
                continue

            pers['full_name'] = account['surname'] + ' ' + account['firstname'] + \
                ' ' + account['patronymic']
            pers['surname'] = account['surname']
            pers['name'] = account['firstname']
            pers['patronymic'] = account['patronymic']
            pers['mobile_phone'] = account['mobile_phone']
            pers['email'] = account['email']
            pers['date_of_birth'] = account['date_of_birth']
            pers['type_role'] = account['type_role']

            hunters[i] = pers

            i += 1

        hunters = self.get_sorted(hunters)

        return hunters

    def get_acc_hunters(self):
        hunters_set = inject.instance(HunterRepository)(self.connection)
        accounts_set = inject.instance(AccountsRepository)(self.connection)

        hunters = hunters_set.get_all()

        if hunters is None:
            return None

        i = 0
        while i < len(hunters):
            pers = hunters[i].get_dict()
            account = accounts_set.get_by_login(pers['login']).get_dict()

            if account['type_role'] != 'охотник':
                hunters.pop(i)
                continue

            pers['full_name'] = account['surname'] + ' ' + account['firstname'] + \
                                ' ' + account['patronymic']
            pers['surname'] = account['surname']
            pers['name'] = account['firstname']
            pers['patronymic'] = account['patronymic']
            pers['mobile_phone'] = account['mobile_phone']
            pers['email'] = account['email']
            pers['date_of_birth'] = account['date_of_birth']
            pers['type_role'] = account['type_role']

            hunters[i] = pers

            i += 1

        hunters = self.get_sorted(hunters)

        return hunters

    def get_by_params(self, data):
        hunters = self.get_all_detailed()

        i = 0
        while i < len(hunters):
            if data['surname'] != '' and hunters[i]['surname'] != data['surname']:
                hunters.pop(i)
                continue
            if data['name'] != '' and hunters[i]['name'] != data['name']:
                hunters.pop(i)
                continue
            if data['patronymic'] != '' and hunters[i]['patronymic'] != data['patronymic']:
                hunters.pop(i)
                continue
            if data['ticket_num'] != '' and hunters[i]['ticket_num'] != data['ticket_num']:
                hunters.pop(i)
                continue

            i += 1

        return hunters


