from django.db import models
from django.db import connection


class Accounts(models.Model):
    login = models.CharField('Логин', max_length=20, primary_key=True)
    pswd = models.TextField('Пароль')

    class Meta:
        db_table = "accounts"

    def __str__(self):
        return self.login


class VouchersDetailed(models.Model):
    id_voucher = models.IntegerField('Идентификатор', primary_key=True)
    animal = models.TextField('Животное')
    amount_animals = models.IntegerField('Количество животных')
    duration_days = models.IntegerField('Количество дней')
    id_sector = models.IntegerField('Идентификатор сектора')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s" % self.id_voucher


class SectorVouchers(models.Model):
    ticket_num = models.IntegerField('Идетификатор охотника')
    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30, default=None)
    date_of_birth = models.DateField('Дата рождения', auto_now=False, auto_now_add=False)
    mobile_phone = models.CharField('Мобильный телефон', max_length=30)
    id_voucher = models.IntegerField('Идетификатор путёвки', primary_key=True)
    animal = models.TextField('Животное')
    amount_animals = models.IntegerField('Количество животных')
    duration_days = models.IntegerField('Количество дней')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)


# Получить все путёвки на конкретного пользователя
def get_vouchers_by_id_hnt(id_hnt):
    '''cursor = connection.cursor()
    cursor.callproc("ShowVouchersByIdHnt", (str(id_hnt),))
    res = cursor.fetchall()
    cursor.close()
    return res'''

    res = VouchersDetailed.objects.raw('SELECT * FROM ShowVouchersByIdHnt(%s);', [id_hnt])
    return res

# Получить все путёвки в конкретном секторе
def get_vouchers_by_id_sct(id_sct):
    res = SectorVouchers.objects.raw('SELECT * FROM ShowVouchersByIdSct(%s);', [id_sct])
    return res

