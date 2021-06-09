from testBL_views.price_list import *
from testBL_views.voucher import *
from testBL_views.account import *
from testBL_views.hunting_grounds import *
from testBL_views.huntsman_views import *


def pricelist_all():
    print('\n' + PriceListView.get_all())

def accounts_all():
    print('\n' + AccountView.get_all())

def cur_vouchers(login):
    vouchers, requests = VoucherView.cur_vouchers(login)
    print("\nОдобренные путёвки\n" + vouchers + '\n')
    print("Заявки\n" + requests)

def is_logged(login, pwd):
    print("Пользователь с таким логином/паролем существует? - ",
          AccountView.is_logged(login, pwd))

def about(login):
    print(AccountView.about(login))

def hunting_grounds_all():
    print(HuntingGroundView.get_all())

def huntsman_all():
    print(HuntsmanView.get_all())

def huntsman_vouchers(login):
    print(VoucherView.huntsman_vouchers(login))

def main():
    while True:
        print('\n' + '-' * 40 + 'MENU' + '-' * 40)
        print("1 - Просмотреть весь прайс-лист\n"
              "2 - Просмотреть все путевки охотника\n"
              "3 - Просмотреть все хозяйства\n"
              "4 - Просмотреть все аккаунты\n"
              "5 - Проверить, существует ли пользователь с данным логином и паролем\n"
              "6 - Информация о пользователе\n"
              "7 - Получить информацию о егерях\n"
              "8 - Просмотреть все путёвки, которые выдал указанный егерь\n"
              "Остальные - Выход\n")

        choice = input("Ваш выбор: ")

        if choice == '1':
            pricelist_all()
        elif choice == '2':
            login = input("Введите логин охотника: ")
            cur_vouchers(login)
        elif choice == '3':
            hunting_grounds_all()
        elif choice == '4':
            accounts_all()
        elif choice == '5':
            login = input("Введите логин: ")
            pwd = input("Введите пароль: ")
            is_logged(login, pwd)
        elif choice == '6':
            login = input("Введите логин: ")
            about(login)
        elif choice == '7':
            huntsman_all()
        elif choice == '8':
            login = input("Введите логин: ")
            huntsman_vouchers(login)
        else:
            return

if __name__ == '__main__':
    main()
