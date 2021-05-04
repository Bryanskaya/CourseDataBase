from man_inject import *
from pattern_repository.hunter_repository import *
from pattern_repository.hunting_grounds_repository import *
from BL_objects import *


if __name__ == '__main__':
    # hunters = inject.instance(HunterRepository)
    # hunters.create(Hunter({'ticket_num': '0000000000',
    #                       'residence': 'г. Москва',
    #                       'login': 'login_test1'}))
    # arr = hunters.get()
    # print(arr)

    # hunting_gr = inject.instance(HuntingGroundsRepository)
    #
    # hunting_gr.create(HuntingGrounds({'id': 2,
    #                                   'ground_name': 'Тест2',
    #                                   'square': '2'}))
    #
    # arr = hunting_gr.get()
    # print(arr)

    # sector = inject.instance(SectorsRepository)
    # sector.create(Sector({'id': 101,
    #                       'square': 1,
    #                       'id_husbandry': 1}))
    # arr = sector.get()
    # print(arr)

    # account = inject.instance(AccountsRepository)
    # account.create(Account({'login': 'login_test2',
    #                        'pswd': 'pswd_test2',
    #                        'surname': 'Иванов',
    #                        'firstname': 'Иван',
    #                        'patronymic': 'Иванов',
    #                        'date_of_birth': '1975-01-01',
    #                        'sex': 'м',
    #                        'mobile_phone': '89000000000',
    #                        'email': 'test_email2@smth.ru',
    #                        'type_role': 'егерь'}))
    # arr = account.get()
    # print(arr)

    # huntsman = inject.instance(HuntsmanRepository)
    # huntsman.create(Huntsman({'id': 101,
    #                           'experience': 1000000,
    #                           'salary': 555,
    #                           'login': 'login_test2'}))
    # arr = huntsman.get()
    # print(arr)

    # pricelist_pos = inject.instance(PriceListRepository)
    # pricelist_pos.create(PriceList({'id': 1001,
    #                                 'animal': 'крот',
    #                                 'price': 10000,
    #                                 'is_relevant': True,
    #                                 'id_sector': 38}))
    # arr = pricelist_pos.get()
    # print(arr)

    # voucher = inject.instance(VoucherRepository)
    # voucher.create(Voucher({'id': 2401,
    #                         'duration_days': 1,
    #                         'amount_animals': 1,
    #                         'price': 500,
    #                         'id_hunter': 35008125,
    #                         'id_pricelist': 108}))
    # arr = voucher.get()
    # print(arr)


