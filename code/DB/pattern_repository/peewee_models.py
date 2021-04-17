from peewee import *
import inject

class BaseModel(Model):
    class Meta:
        database = inject.instance(////////)

class accounts(BaseModel):
    pass

class hunters(BaseModel):
    ticket_num = IntegerField(column_name='ticket_num', primary_key=True)
    surname = TextField(column_name='surname')
    firstname = TextField(column_name='surname')
    patronymic = TextField(column_name='surname')
    date_of_birth = DateTimeField(column_name='date_of_birth')
    sex = CharField(column_name='sex')
    residence = TextField(column_name='residence')
    mobile_phone = TextField(column_name='mobile_phone')
    email = TextField(column_name='email')
    login = TextField(column_name='login')
    #login = ForeignKeyField(accounts, column_name='login')