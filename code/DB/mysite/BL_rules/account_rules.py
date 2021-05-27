import hashlib, uuid

import sys
sys.path.append("..")

from inject_config import *
from BL_rules.base_rules import *
from errors.err_account import *


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
        print("PASSWORD: \n", hashed_password, account.get_hashed_password())
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
        account = accounts_set.get_by_login(login)

        return account

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

    def delete_account(self, obj: Account):
        accounts_set = inject.instance(AccountsRepository)(self.connection)
        accounts_set.delete(obj)






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
    roles = ['администратор', 'охотник', 'егерь']


class HunterRoleCheck(RoleCheck):
    roles = ['администратор', 'охотник']


class HuntsmanRoleCheck(RoleCheck):
    roles = ['администратор', 'егерь']


class AdminRoleCheck(RoleCheck):
    roles = ['администратор']