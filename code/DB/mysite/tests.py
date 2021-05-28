import unittest

from inject_config import *
from datetime import *

from pattern_repository.accounts_repository import *
from pattern_repository.hunter_repository import *
from pattern_repository.hunting_grounds_repository import *
from pattern_repository.huntsman_repository import *
from pattern_repository.price_list_repository import *
from pattern_repository.sectors_repository import *
from pattern_repository.voucher_repository import *

class BaseTests(object):
    conn = SqliteDatabase(':memory:')
    rep = None

    objects = []
    updated_object = None

    @staticmethod
    def get_sorted(arr):
        raise NotImplementedError

    @staticmethod
    def is_equal_len(set1, set2):
        return len(set1) == len(set2)

    def is_equal_data(self, set1, set2):
        if not BaseTests.is_equal_len(set1, set2):
            return False

        set1_sorted = self.get_sorted(set1)
        set2_sorted = self.get_sorted(set2)

        for i in range(len(set1)):
            if set1_sorted[i] != set2_sorted[i]:
                return False

        return True

    def setUp(self):
        for obj in self.objects:
            self.rep.create(obj)

    def tearDown(self):
        self.conn.close()

    def test_delete(self):
        set = self.objects.copy()
        elem = set.pop(0)

        self.rep.delete(elem)
        set_rep = self.rep.get_all()

        self.assertTrue(self.is_equal_len(set, set_rep))
        self.assertTrue(self.is_equal_data(set, set_rep))

    def test_update(self):
        set = self.objects.copy()

        self.rep.update(set[0], self.updated_object)
        set[0] = self.updated_object

        set_rep = self.rep.get_all()

        self.assertTrue(self.is_equal_len(set, set_rep))
        self.assertTrue(self.is_equal_data(set, set_rep))

    def test_get_all(self):
        obj_set = self.rep.get_all()

        self.assertTrue(self.is_equal_len(self.objects, obj_set))
        self.assertTrue(self.is_equal_data(self.objects, obj_set))


class AccountRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_AccountsRepository(conn)
    updated_object = Account({'login': '00000000', 'salt': 'aaaaa', 'hashed_password': '01010101', 'surname': 'Петрова',
                'firstname': 'Фёкла', 'patronymic': '', 'date_of_birth': date(2000, 1, 1),
                'sex': 'ж', 'mobile_phone': '+7-999-888-77-66', 'email': 'qwe@mail.ru', 'type_role': 'охотник'})

    objects = [
        Account({'login': '00000000', 'salt': 'aaaaa', 'hashed_password': '01010101', 'surname': 'Петров',
                'firstname': 'Фёдор', 'patronymic': '', 'date_of_birth': date(2000, 1, 1),
                'sex': 'м', 'mobile_phone': '+7-000-000-00-00', 'email': 'qwe@mail.ru', 'type_role': 'охотник'}),
        Account({'login': '00000001', 'salt': 'bbbbb', 'hashed_password': '02020202', 'surname': 'Бирюкова',
                'firstname': 'Юля', 'patronymic': 'Ивановна', 'date_of_birth': date(1999, 5, 6),
                'sex': 'ж', 'mobile_phone': '+7-999-999-99-99', 'email': 'abc@mail.ru', 'type_role': 'егерь'}),
        Account({'login': '00000002', 'salt': 'ccccc', 'hashed_password': '03030303', 'surname': 'Мягкова',
                'firstname': 'Женя', 'patronymic': 'Георгиевна', 'date_of_birth': date(2005, 11, 11),
                'sex': 'ж', 'mobile_phone': '+7-111-999-88-88', 'email': 'qweasdzxc@mail.ru', 'type_role': 'охотник'}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.login)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([AccountModel])
        super(AccountRepositoryTest, self).setUp()

    def test_get_by_login(self):
        person = self.rep.get_by_login(self.objects[0].login)
        self.assertEqual(person, self.objects[0])

class HunterRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_HunterRepository(conn)
    updated_object = Hunter({'ticket_num': '99999999', 'residence': 'Россия', 'login': '00000000'})

    objects = [
        Hunter({'ticket_num': '99999999', 'residence': 'Китай', 'login': '00000000'}),
        Hunter({'ticket_num': '88888888', 'residence': 'Россия', 'login': '00000001'}),
        Hunter({'ticket_num': '77777777', 'residence': 'Украина', 'login': '00000002'}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.ticket_num)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([HunterModel])
        super(HunterRepositoryTest, self).setUp()

    def test_get_by_ticket_num(self):
        person = self.rep.get_by_ticket_num(self.objects[0].ticket_num)
        self.assertEqual(person, self.objects[0])

class HuntingGroundsRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_HuntingGroundsRepository(conn)
    updated_object = HuntingGrounds({'id': 1000, 'ground_name': 'Московская область'})

    objects = [
        HuntingGrounds({'id': 1000, 'ground_name': 'Рязанская область'}),
        HuntingGrounds({'id': 1001, 'ground_name': 'Крым'}),
        HuntingGrounds({'id': 1002, 'ground_name': 'Владимирская область'}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.id)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([HuntingGroundsModel])
        super(HuntingGroundsRepositoryTest, self).setUp()

    def test_get_by_id(self):
        ground = self.rep.get_by_id(self.objects[0].id)
        self.assertEqual(ground, self.objects[0])

class HuntsmanRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_HuntsmanRepository(conn)
    updated_object = Huntsman({'id': 22222222, 'login': '00000003'})

    objects = [
        Huntsman({'id': 22222222, 'login': '00000000'}),
        Huntsman({'id': 33333333, 'login': '00000001'}),
        Huntsman({'id': 44444444, 'login': '00000002'}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.id)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([HuntsmanModel])
        super(HuntsmanRepositoryTest, self).setUp()

    def test_get_by_id(self):
        person = self.rep.get_by_id(self.objects[0].id)
        self.assertEqual(person, self.objects[0])

class PriceListRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_PriceListRepository(conn)
    updated_object = PriceList({'id': 1, 'animal': 'утка',
                                'price': 320, 'is_relevant': True, 'id_sector': 99999999})

    objects = [
        PriceList({'id': 1, 'animal': 'лось',
                   'price': 10000, 'is_relevant': False, 'id_sector': 99999999}),
        PriceList({'id': 11, 'animal': 'бобр',
                   'price': 5000, 'is_relevant': False, 'id_sector': 77777777}),
        PriceList({'id': 111, 'animal': 'гусь',
                    'price': 3500, 'is_relevant': True, 'id_sector': 99999999}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.id)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([PriceListModel])
        super(PriceListRepositoryTest, self).setUp()

    def test_get_by_id(self):
        pos = self.rep.get_by_id(self.objects[0].id)
        self.assertEqual(pos, self.objects[0])

class SectorRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_PriceListRepository(conn)
    updated_object = Sector({'id': 207, 'id_husbandry': 1000})

    objects = [
        Sector({'id': '101', 'id_husbandry': 1001}),
        Sector({'id': '203', 'id_husbandry': 1001}),
        Sector({'id': '207', 'id_husbandry': 1002}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.id)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([SectorModel])
        super(SectorRepositoryTest, self).setUp()

    def test_get_by_id(self):
        sector = self.rep.get_by_id(self.objects[0].id)
        self.assertEqual(sector, self.objects[0])
'''
class VoucherRepositoryTest(BaseTests, unittest.TestCase):
    conn = SqliteDatabase(':memory:')
    rep = PW_PriceListRepository(conn)
    updated_object = Voucher({'id': 1000001, 'duration_days': 5, 'amount_animals': 3,
                             'price': 5000, 'id_hunter': 99999999, 'id_pricelist': 111})

    objects = [
        Voucher({'id': 1000001, 'duration_days': 5, 'amount_animals': 3,
                 'price': 5000, 'id_hunter': 99999999, 'id_pricelist': 1}),
        Voucher({'id': 1000002, 'duration_days': 14, 'amount_animals': 1,
                 'price': 3700, 'id_hunter': 99999999, 'id_pricelist': 1}),
        Voucher({'id': 1000003, 'duration_days': 60, 'amount_animals': 15,
                 'price': 6800, 'id_hunter': 77777777, 'id_pricelist': 11}),
    ]

    @staticmethod
    def get_sorted(arr):
        return sorted(arr, key=lambda x: x.id)

    def setUp(self):
        self.conn.connect()
        self.conn.create_tables([VoucherModel])
        super(VoucherRepositoryTest, self).setUp()

    def test_get_by_id(self):
        voucher = self.rep.get_by_id(self.objects[0].id)
        self.assertEqual(voucher, self.objects[0])
'''

if __name__ == '__main__':
    unittest.main()

