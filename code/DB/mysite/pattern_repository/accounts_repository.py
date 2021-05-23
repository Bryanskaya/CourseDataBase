from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.accounts import *
from errors.err_account import *


class AccountsRepository(Repository):
    def create(self, obj: Account):
        raise NotImplementedError

    def delete(self, obj: Account):
        raise NotImplementedError

    def get_all(self) -> [Account]:
        raise NotImplementedError

    def get_by_login(self, login) -> Account:
        raise NotImplementedError

    def is_relevant_password(self, password: str):
        raise NotImplementedError


class PW_AccountsRepository(AccountsRepository):
    def create(self, obj: Account):
        try:
            AccountModel.create(login=obj.get_login(),
                                salt=obj.get_salt(),
                                hashed_password=obj.get_hashed_password(),
                                surname=obj.get_surname(),
                                firstname=obj.get_firstname(),
                                patronymic=obj.get_patronymic(),
                                date_of_birth=obj.get_date_of_birth(),
                                sex=obj.get_sex(),
                                mobile_phone=obj.get_mobile_phone(),
                                email=obj.get_email(),
                                type_role=obj.get_type_role())
        except:
            raise CreateBLObjectAccountErr()

    def delete(self, obj: Account):
        temp = AccountModel.delete().where(AccountModel.login == obj.login)
        temp.execute()

    def get_all(self) -> [Account]:
        temp = AccountModel.select()
        return transf_to_objs(temp, Account)

    def get_by_login(self, login: str) -> Account:
        temp = AccountModel.select().where(AccountModel.login == login)
        accounts_set = transf_to_objs(temp, Account)

        if len(accounts_set):
            return accounts_set[0]
        return None

