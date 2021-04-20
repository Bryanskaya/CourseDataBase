from peewee import *
import inject

from pattern_repository.repository import CurConnection


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
    pswd = TextField(column_name='pswd')
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
    #login = TextField(column_name='login')
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





