from man_inject import *
from pattern_repository.hunter_repository import *
from pattern_repository.hunting_grounds_repository import *
from BL_objects import *


if __name__ == '__main__':
    # hunters = inject.instance(HunterRepository)
    # hunters.create(Hunter({'ticket_num': '0000000000',
    #                       'surname': 'Иванов',
    #                       'firstname': 'Иван',
    #                       'patronymic': 'Иванович',
    #                       'date_of_birth': '01.01.2000',
    #                       'sex': 'м',
    #                       'residence': 'г. Москва',
    #                       'mobile_phone': '8 910 000 00 00',
    #                       'email': 'smth@main.ru',
    #                       'login': 'IvaIv_01_01_2000'}))
    '''arr = hunters.get()
    print(arr)'''

    hunting_gr = inject.instance(HuntingGroundsRepository)

    hunting_gr.create(HuntingGrounds({'id': 2,
                                      'ground_name': 'Тест2',
                                      'square': '2'}))

    arr = hunting_gr.get()
    print(arr)
