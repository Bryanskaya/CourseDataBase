from BL_rules.account_rules import *
from .base import *


class AccountView(BaseView):
    @classmethod
    def is_logged(cls, login, pwd):
        acc_rules = AccountRules('admin')
        account = acc_rules.is_log_in(login, pwd)
        return account is not None

    @classmethod
    def about(cls, login):
        acc_rules = AccountRules('admin')
        acc = acc_rules.get_person(login)

        if acc is not None:
            return cls.dict_to_str(acc.get_dict())
        return "ОШИБКА: такого логина нет в БД"

    @classmethod
    def get_all(cls):
        acc_rules = AccountRules('admin')
        accounts = acc_rules.get_all()

        return cls.set_to_str(accounts)