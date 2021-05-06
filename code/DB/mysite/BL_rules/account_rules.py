import sys
sys.path.append("..")

from inject_config import *


class AccountRules(object):
    @staticmethod
    def is_relevant_password(account, password):
        if account.get_password() == password:
            return True #TODO проверка пароля
        return False

    @staticmethod
    def is_log_in(login, password):
        accounts_set = inject.instance(AccountsRepository)
        account = accounts_set.get_by_login(login)

        if not len(account):
            return False
        elif AccountRules.is_relevant_password(account[0], password):
            return account[0].get_dict()  #TODO где прокинуть страницу
        else:
            return False

    @staticmethod
    def get_person(login):
        accounts_set = inject.instance(AccountsRepository)
        return accounts_set.get_by_login(login)[0].get_dict()
