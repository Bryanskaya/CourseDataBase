from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.accounts import *
from errors.err_account import *


class AccountsRepository(Repository):
    def create(self, obj: Account):
        raise NotImplementedError

    def delete(self, obj: Account):
        raise NotImplementedError

    def accept(self, login: str):
        raise NotImplementedError

    def update(self, obj_old: Account, obj_upd: Account):
        raise NotImplementedError

    def update_password(self, login, password):
        raise NotImplementedError

    def get_all(self) -> [Account]:
        raise NotImplementedError

    def get_by_login(self, login) -> Account:
        raise NotImplementedError

    def is_relevant_password(self, password: str):
        raise NotImplementedError


class PW_AccountsRepository(AccountsRepository):
    model = None

    def __init__(self, connection):
        self.model = AccountModel(connection)

    def create(self, obj: Account):
        try:
            self.model.insert(login=obj.get_login(),
                                salt=obj.get_salt(),
                                hashed_password=obj.get_hashed_password(),
                                surname=obj.get_surname(),
                                firstname=obj.get_firstname(),
                                patronymic=obj.get_patronymic(),
                                date_of_birth=obj.get_date_of_birth(),
                                sex=obj.get_sex(),
                                mobile_phone=obj.get_mobile_phone(),
                                email=obj.get_email(),
                                type_role=obj.get_type_role()).execute()
        except:
            raise CreateBLObjectAccountErr()

    def delete(self, obj: Account):
        temp = self.model.delete().where(AccountModel.login == obj.login)
        temp.execute()

    def accept(self, login: str):
        try:
            pers = self.get_by_login(login)
            self.model.update(type_role=pers.type_role[1:]).where(AccountModel.login == login).execute()
        except:
            raise AcceptAccountErr()

    def reject(self, login: str):
        try:
            self.model.delete().where(AccountModel.login == login).execute()
        except:
            raise DeleteAccountErr()

    def update(self, obj_old: Account, obj_upd: Account):
        if self.get_by_login(obj_old.login) is None:
            raise LoginAccountNotExists()

        temp = self.model.update(obj_upd.get_dict()).where(AccountModel.login == obj_upd.login)
        try:
            temp.execute()
        except:
            raise UpdateAccountErr()

    def update_password(self, login, password):
        if self.get_by_login(login) is None:
            raise LoginAccountNotExists()

        temp = self.model.update(hashed_password=password).where(AccountModel.login == login)
        try:
            temp.execute()
        except:
            raise UpdateAccountErr()

    def get_all(self) -> [Account]:
        temp = self.model.select()
        return transf_to_objs(temp, Account)

    def get_acc_admins(self) -> [Account]:
        temp = self.model.select().where(AccountModel.type_role == "админ")
        return transf_to_objs(temp, Account)

    def get_by_login(self, login: str) -> Account:
        temp = self.model.select().where(AccountModel.login == login)
        accounts_set = transf_to_objs(temp, Account)

        if len(accounts_set):
            return accounts_set[0]
        return None

