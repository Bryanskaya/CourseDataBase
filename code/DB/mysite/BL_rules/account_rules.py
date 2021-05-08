import hashlib, uuid

import sys
sys.path.append("..")

from inject_config import *
from errors.err_account import *


class AccountRules(object):
    valuable_roles = {
        'администратор': 'admin',
        'охотник': 'hunter',
        'егерь': 'huntsman'
    }

    @staticmethod
    def get_role_eng(role):
        if role in AccountRules.valuable_roles.keys():
            return AccountRules.valuable_roles[role]
        else:
            return role

    @staticmethod
    def make_password_hashed(password, salt):
        salt_password = password.encode('utf-8') + salt.encode('utf-8')
        return hashlib.sha256(salt_password).hexdigest()

    @staticmethod
    def is_relevant_password(account, password):
        salt = account.get_salt()
        hashed_password = AccountRules.make_password_hashed(password, salt)
        print("PASSWORD: %s %s\n", hashed_password, account.get_hashed_password())
        return hashed_password == account.get_hashed_password()

    @staticmethod
    def is_log_in(login, password):
        accounts_set = inject.instance(AccountsRepository)
        account = accounts_set.get_by_login(login)

        if account is None:
            return None
        elif AccountRules.is_relevant_password(account, password):
            return account
        else:
            print("***********password*******\n",)
            return None

    @staticmethod
    def get_person(login):
        accounts_set = inject.instance(AccountsRepository)
        return accounts_set.get_by_login(login)

    @staticmethod
    def get_cookie(account: Account) -> dict:
        res_dict = {
            'login': account.get_login(),
            'role': account.get_type_role(),
            'role_eng': AccountRules.get_role_eng(account.get_type_role()),
        }

        return res_dict


class BaseAccountCheck(object):
    def check(self, data: dict):
        if 'login' not in data.keys():
            raise AuthorisedErr()
        if 'role' not in data.keys():
            raise AuthorisedErr()


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