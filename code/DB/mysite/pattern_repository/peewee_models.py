from pattern_repository.repository import CurConnection
from peewee import *
import inject


def transf_to_objs(data, to_class):
    arr = []

    for temp in data.dicts():
        arr.append(to_class(temp))

    return arr


class BaseModel(Model):
    class Meta:
        database = inject.instance(CurConnection)


class AccountModel(BaseModel):
    login = TextField(column_name='login', primary_key=True)
    salt = TextField(column_name='salt')
    hashed_password = TextField(column_name='hashed_password')
    surname = TextField(column_name='surname')
    firstname = TextField(column_name='firstname')
    patronymic = TextField(column_name='patronymic')
    date_of_birth = DateTimeField(column_name='date_of_birth')
    sex = CharField(column_name='sex')
    mobile_phone = TextField(column_name='mobile_phone')
    email = TextField(column_name='email')
    type_role = TextField(column_name='type_role')

    class Meta:
        table_name = 'accounts'

class HunterModel(BaseModel):
    ticket_num = IntegerField(column_name='ticket_num', primary_key=True)
    residence = TextField(column_name='residence')
    login = ForeignKeyField(AccountModel, column_name='login')

    class Meta:
        table_name = 'hunters'


class HuntingGroundsModel(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    ground_name = TextField(column_name='ground_name')
    square = FloatField(column_name='square')

    class Meta:
        table_name = 'hunting_grounds'


class SectorModel(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    square = FloatField(column_name='square')
    id_husbandry = ForeignKeyField(HuntingGroundsModel, column_name='id_husbandry')

    class Meta:
        table_name = 'sectors'


class HuntsmanModel(BaseModel):
    id = ForeignKeyField(SectorModel, column_name='id', primary_key=True)
    login = ForeignKeyField(AccountModel, column_name='login')

    class Meta:
        table_name = 'huntsmen'


class PriceListModel(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    animal = TextField(column_name='animal')
    price = FloatField(column_name='price')
    is_relevant = BooleanField(column_name='is_relevant')
    id_sector = ForeignKeyField(SectorModel, column_name='id_sector')

    class Meta:
        table_name = 'price_list'


class VoucherModel(BaseModel):
    id = IntegerField(column_name='id', primary_key=True)
    duration_days = IntegerField(column_name='duration_days')
    amount_animals = IntegerField(column_name='amount_animals')
    price = FloatField(column_name='price')
    id_hunter = ForeignKeyField(HunterModel, column_name='id_hunter')
    id_pricelist = ForeignKeyField(PriceListModel, column_name='id_pricelist')

    class Meta:
        table_name = 'vouchers'






