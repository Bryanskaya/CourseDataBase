from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.accounts import *
from pattern_repository.errors import *


class AccountsRepository(Repository):
    def __init__(self):
        pass


class PW_AccountsRepository(AccountsRepository):
    def __init__(self):
        pass

    def create(self, obj: Account):
        # try:
        AccountModel.create(login=obj.get_login(),
                            pswd=obj.get_password(),
                            surname=obj.get_surname(),
                            firstname=obj.get_firstname(),
                            patronymic=obj.get_patronymic(),
                            date_of_birth=obj.get_date_of_birth(),
                            sex=obj.get_sex(),
                            mobile_phone=obj.get_mobile_phone(),
                            email=obj.get_email(),
                            type_role=obj.get_type_role())
    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = AccountModel.select()

        return transf_to_objs(temp, Account)
