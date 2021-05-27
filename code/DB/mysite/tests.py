import unittest

from inject_config import *
from datetime import *

from pattern_repository.accounts_repository import *

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



if __name__ == '__main__':
    unittest.main()

