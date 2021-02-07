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


class PriceListSector(models.Model):
    id_pos = models.IntegerField('Идетификатор путёвки в прайс-листе', primary_key=True)
    animal = models.TextField('Животное')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    id_sector = models.IntegerField('Идентификатор сектора')
    name_ground = models.CharField('Название сектора', max_length=30)


class GenPrices(models.Model):
    class Meta:
        unique_together = (('ground_name', 'id_sector', 'animal', 'num', 'price'),)

    ground_name = models.CharField('Название хозяйства', max_length=30, primary_key=True)
    id_sector = models.IntegerField('Идентификатор сектора')
    animal = models.TextField('Животное')
    num = models.IntegerField('Количество выданных путёвок')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)


class GenHuntsmen(models.Model):
    ground_name = models.CharField('Название хозяйства', max_length=30)
    id_sector = models.IntegerField('Идентификатор сектора', primary_key=True)
    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30, default=None)
    mobile_phone = models.CharField('Телефон', max_length=30)
    email = models.CharField('Почта', max_length=40)


class GenHunters(models.Model):
    ticket_num = models.IntegerField('Идетификатор охотника', primary_key=True)
    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30, default=None)
    date_of_birth = models.DateField('Дата рождения', auto_now=False, auto_now_add=False)
    sex = models.CharField('Пол', max_length=1)
    mobile_phone = models.CharField('Телефон', max_length=30)
    email = models.CharField('Почта', max_length=40)
    residence = models.CharField('Прописка', max_length=100)
    id_voucher = models.IntegerField('Идетификатор путёвки')
    animal = models.TextField('Животное')
    num_animals = models.IntegerField('Количество выданных путёвок')
    num_days = models.IntegerField('Количество дней')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    id_sector = models.IntegerField('Идентификатор сектора')


class HuntersSector(models.Model):
    ticket_num = models.IntegerField('Идетификатор охотника')
    surname = models.CharField('Фамилия', max_length=30)
    firstname = models.CharField('Имя', max_length=30)
    patronymic = models.CharField('Отчество', max_length=30, default=None)
    mobile_phone = models.CharField('Телефон', max_length=30)
    email = models.CharField('Почта', max_length=40)
    id_voucher = models.IntegerField('Идетификатор путёвки', primary_key=True)
    animal = models.TextField('Животное')
    num_animals = models.IntegerField('Количество выданных путёвок')
    num_days = models.IntegerField('Количество дней')
    price = models.DecimalField('Цена', max_digits=5, decimal_places=2)
    id_sector = models.IntegerField('Идентификатор сектора')

# Ф   У   Н   К   Ц   И   И

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


# Прайс-лист путёвок только в секторе под номером (номер вводится)
def get_price_list_by_id_sct(id_sct):
    res = PriceListSector.objects.raw('SELECT * FROM ShowPriceListByIdSct(%s);', [id_sct])
    return res


# Получить информацию следующего вида:
# название хозяйства - номер сектора - название животного - количество выданных путёвок - средняя цена
def get_general_info_prices():
    res = GenPrices.objects.raw('SELECT * FROM ShowDeneralInfoPrices();')
    return res


# Получить информацию вида: название хозяйства - номер сектора - ФИО егеря + контакты
def get_huntsmen():
    res = GenHuntsmen.objects.raw('SELECT * FROM ShowHuntmen();')
    return res


# Найти охотника по ФИО и получить подробнейшую инфу о нём (включая все путёвки, которые у него есть)
def get_hunters_by_SFP(t_surname, t_firstname, t_patronymic):
    res = GenHunters.objects.raw('SELECT * FROM ShowHuntersBySFP(%s, %s, %s);', [t_surname, t_firstname, t_patronymic])
    return res


# Получить всех охотников, которых охотятся в конкретном секторе
def get_hunters_by_id_sct(id_sct):
    res = HuntersSector.objects.raw('SELECT * FROM ShowHuntersByIdSct(%s);', [id_sct])
    return res


# П   Р   О   Ц   Е   Д   У   Р   Ы
# Выдать новую путёвку
def proc_add_voucher(num_days, num_animals, price, id_hnt, id_prclist):
    cursor = connection.cursor()
    cursor.execute("CALL AddVoucher(%s, %s, %s, %s, %s);", (str(num_days), str(num_animals), str(price), str(id_hnt), str(id_prclist),))
    connection.commit()     # нужно ли оно вообще
    cursor.close()
    return None     # Странное дело, без него ошибка


# Удалить (закрыть) путёвку по её id
def proc_delete_voucher(id_vch):
    cursor = connection.cursor()
    cursor.execute("CALL DelVoucher(%s);", (str(id_vch),))
    connection.commit()  # нужно ли оно вообще
    cursor.close()
    return None  # Странное дело, без него ошибка


# Пометить позицию в прайс листе сектора как неактуальную
def proc_mark_point_pricelist_irrelevant(name_animal, id_sct):
    cursor = connection.cursor()
    cursor.execute("CALL MarkPointPriceListIrrelevant(%s, %s);", (str(name_animal), str(id_sct),))
    connection.commit()  # нужно ли оно вообще
    cursor.close()
    return None  # Странное дело, без него ошибка


#  Добавить позицию в прайс лист
def proc_add_point_pricelist(name_animal, price, id_sct):
    cursor = connection.cursor()
    cursor.execute("CALL AddPointPriceList(%s, %s, %s);", (str(name_animal), str(price), str(id_sct),))
    connection.commit()  # нужно ли оно вообще
    cursor.close()
    return None  # Странное дело, без него ошибка



