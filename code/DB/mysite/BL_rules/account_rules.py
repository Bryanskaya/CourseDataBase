import hashlib, uuid

import sys
sys.path.append("..")

from inject_config import *
from BL_rules.base_rules import *
from errors.err_account import *
from BL_rules.huntsman_rules import *
from BL_rules.voucher_rules import *
from mail.send_email import *


class AccountRules(BaseRules):
    valuable_roles = {
        'админ': 'admin',
        'охотник': 'hunter',
        'егерь': 'huntsman'
    }

    @staticmethod
    def generate_salt():
        return uuid.uuid4().hex

    @staticmethod
    def get_role_eng(role):
        if role in AccountRules.valuable_roles.keys():
            return AccountRules.valuable_roles[role]
        else:
            return role

    @staticmethod
    def get_roles():
        return AccountRules.valuable_roles

    @staticmethod
    def make_password_hashed(password, salt):
        salt_password = password.encode('utf-8') + salt.encode('utf-8')
        return hashlib.sha256(salt_password).hexdigest()

    @staticmethod
    def is_relevant_password(account, password):
        salt = account.get_salt()
        hashed_password = AccountRules.make_password_hashed(password, salt)
        #print("PASSWORD: \n", hashed_password, account.get_hashed_password())
        return hashed_password == account.get_hashed_password()

    def is_log_in(self, login, password):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        account = accounts_set.get_by_login(login)

        if account is None:
            return None
        elif AccountRules.is_relevant_password(account, password):
            return account
        else:
            return None

    def is_exist_login(self, login):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        return accounts_set.get_by_login(login)

    def get_person(self, login):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        return accounts_set.get_by_login(login)

    @staticmethod
    def get_cookie(account: Account) -> dict:
        res_dict = {
            'login': account.get_login(),
            'role': account.get_type_role(),
            'role_eng': AccountRules.get_role_eng(account.get_type_role()),
        }

        return res_dict

    def register(self, login, password, surname, firstname, patronymic, date_of_birth,
                 sex, mobile_phone, email, type_role):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        exist_account = accounts_set.get_by_login(login)

        if exist_account is not None:
            print("///// exist login\n")
            return None     #TODO message about existing account

        type_role = '#' + type_role
        salt = AccountRules.generate_salt()
        hashed_password = AccountRules.make_password_hashed(password, salt)

        account = Account(locals())
        try:
            accounts_set.create(account)
        except CreateBLObjectAccountErr:
            print("///// error in create\n")
            account = None

        return account

    def accept(self, login):
        acc_rep = inject.instance(AccountsRepository)(self.connection)
        acc_rep.accept(login)

    def reject(self, login):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        accounts_set.reject(login)

    def reject_admin(self, login):
        self.reject(login)

    def reject_hunter(self, login):
        vouchers_rules = VoucherRules('', self.connection)
        hunters_rules = HunterRules('', self.connection)

        hunter = hunters_rules.get_by_login(login).get_dict()

        vouchers_rules.delete_by_huntsman(hunter['ticket_num'])
        hunters_rules.delete_by_huntsman(hunter['ticket_num'])
        self.reject(login)

    def reject_huntsman(self, login):
        huntsman_rules = HuntsmanRules('', self.connection)

        huntsman_rules.reject(login)
        self.reject(login)

    def delete_account(self, obj: Account):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        accounts_set.delete(obj)

    def get_sorted(self, arr: [Account]):
        return sorted(arr, key=lambda x: (x['login'], x['surname'],
                                           x['firstname'], x['patronymic'],
                                          x['date_of_birth']))

    def get_all(self):
        acc_rep = inject.instance(AccountsRepository)(self.connection)
        accounts = acc_rep.get_all()

        for i in range(len(accounts)):
            accounts[i] = accounts[i].get_dict()

        accounts = self.get_sorted(accounts)

        return accounts

    def get_req_admins(self):
        acc_rep = inject.instance(AccountsRepository)(self.connection)
        accounts = acc_rep.get_all()

        for i in range(len(accounts)):
            accounts[i] = accounts[i].get_dict()

        i = 0
        while i < len(accounts):
            if accounts[i]['type_role'] != '#админ':
                accounts.pop(i)
                continue
            i += 1

        return accounts

    def get_acc_admins(self):
        acc_rep = inject.instance(AccountsRepository)(self.connection)
        accounts = acc_rep.get_all()

        for i in range(len(accounts)):
            accounts[i] = accounts[i].get_dict()

        i = 0
        while i < len(accounts):
            if accounts[i]['type_role'] != 'админ':
                accounts.pop(i)
                continue
            i += 1

        return accounts

    def get_by_params(self, data):
        accounts = self.get_all()

        i = 0

        while i < len(accounts):
            if data['surname'] != '' and accounts[i]['surname'] != data['surname']:
                accounts.pop(i)
                continue
            if data['name'] != '' and accounts[i]['firstname'] != data['name']:
                accounts.pop(i)
                continue
            if data['patronymic'] != '' and accounts[i]['patronymic'] != data['patronymic']:
                accounts.pop(i)
                continue

            i += 1

        return accounts

    def send_recover(self, obj: Account):
        email = obj.get_email()
        inject.instance(MailManager).generate_mail(email)

    def check_recover(self, data: dict):
        cur_code = data['num1'] + data['num2'] + \
                   data['num3'] + data['num4']

        cnt_code = inject.instance(MailManager).get_code(data['email'])
        if cnt_code != cur_code:
            raise WrongCode()

        if data['password'] != data['repeated_password']:
            raise DifferPasswords()

        acc_rep = inject.instance(AccountsRepository)(self.connection)
        account = acc_rep.get_by_login(data['login'])

        hashed_pwd = self.make_password_hashed(data['password'], account.get_salt())
        acc_rep.update_password(data['login'], hashed_pwd)






class BaseAccountCheck(object):
    def check(self, data: dict):
        if 'login' not in data.keys():
            raise AuthorisedErr() #TODO логина нет
        if 'role' not in data.keys():
            raise AuthorisedErr() #TODO развести еще не рассмотреные заявки и отклоненные


class RoleCheck(BaseAccountCheck):
    roles = []

    def check(self, data: dict):
        super().check(data)

        if data['role'] not in self.roles:
            raise WrongRoleErr()


class AllRolesCheck(RoleCheck):
    roles = ['админ', 'охотник', 'егерь']


class HunterRoleCheck(RoleCheck):
    roles = ['админ', 'охотник']


class HuntsmanRoleCheck(RoleCheck):
    roles = ['админ', 'егерь']


class AdminRoleCheck(RoleCheck):
    roles = ['админ']