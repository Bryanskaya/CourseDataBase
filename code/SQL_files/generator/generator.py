from faker import Faker
from random import choice
import secrets
import pytils.translit  #


NUM_SECTORS = 100
MAX_AMOUNT = 1000

animals = ['утка', 'гусь', 'тетерев', 'заяц-русак', 'лиса',
           'бобёр', 'выдра', 'косуля', 'лось', 'рябчик',
           'олень', 'бекас', 'медведь', 'волк', 'кабан',
           'глухарь', 'перепел', 'куропатка', 'заяц-беляк', 'барсук',
           'куница', 'норка', 'вальдшнеп', 'куропатка', 'перепел',
           'кряква', 'чернеть', 'чирок', 'ондатра', 'хорёк']
price = [i for i in range(300, 8000, 150)]
huntsmen_sectors = [i+1 for i in range(NUM_SECTORS)]
sex = ['м', 'ж']
login = []
hunters = []


def generate_hunting_grounds():
    fake_ru = Faker('ru_Ru')

    f = open('hunting_grounds.cvg', 'w')
    temp = []
    i = 0

    while i < 70:
        name = fake_ru.region()
        if name not in temp:
            temp.append(name)
        else:
            continue

        s = choice(range(100, 10000))

        line = "{0}|{1}\n".format(
            name,
            s
        )

        f.write(line)
        i += 1
    f.close()


def generate_sectors():
    f = open('sectors.cvg', 'w')

    i = 1
    while i <= NUM_SECTORS:
        id_husbandry = choice(range(1, 70))

        s = choice(range(100, 10000))

        line = "{0}|{1}\n".format(
            s,
            id_husbandry
        )

        f.write(line)
        i += 1
    f.close()


def generate_price_list():
    f = open('price_list.cvg', 'w')
    temp = []
    for i in range(NUM_SECTORS + 1):
        temp.append([] * len(animals))
    i = 0

    while i < MAX_AMOUNT:
        animal = secrets.choice(animals)
        prc = choice(price)
        id_sector = choice(range(1, NUM_SECTORS))
        is_relevant = True

        if animal in temp[id_sector]:
            continue

        line = "{0}|{1}|{2}|{3}\n".format(
            animal,
            prc,
            is_relevant,
            id_sector
        )

        temp[id_sector].append(animal)
        f.write(line)

        i += 1

    f.close()


def generate_huntsmen():
    f = open('huntsmen.cvg', 'w', encoding='utf-8')

    i = 0
    while i < NUM_SECTORS:
        ind = choice(range(len(huntsmen_sectors)))
        id_sector = huntsmen_sectors[ind]
        del huntsmen_sectors[ind]

        experience = choice(range(0, 50))
        salary = choice(range(10000, 80000, 5000))
        lgn = login[i]

        line = "{0}|{1}|{2}|{3}\n".format(
            id_sector,
            experience,
            salary,
            lgn
        )

        f.write(line)
        i += 1
    f.close()


def generate_hunters():
    fake_ru = Faker('ru_Ru')

    f = open('hunters.cvg', 'w')

    for i in range(MAX_AMOUNT):
        address = fake_ru.address()
        num_ticket = fake_ru.ean(length = 8)
        hunters.append(num_ticket)

        lgn = login[NUM_SECTORS + i]

        line = "{0}|{1}|{2}\n".format(
                num_ticket,
                address,
                lgn)

        f.write(line)
    f.close()


def generate_accounts():
    fake = Faker()
    fake_ru = Faker('ru_Ru')

    f = open('accounts.cvg', 'w')

    i = 0
    while i < NUM_SECTORS + MAX_AMOUNT:
        sex_p = choice(sex)
        if sex_p == 'м':
            surname = fake_ru.last_name_male()
            name = fake_ru.first_name_male()
            patronymic = fake_ru.middle_name_male()
        else:
            surname = fake_ru.last_name_female()
            name = fake_ru.first_name_female()
            patronymic = fake_ru.middle_name_female()

        date_of_brth = fake_ru.date_of_birth(None, 21, 80)
        phone = fake_ru.phone_number()
        email = fake_ru.email()

        lgn = surname[:3] + name[:2] + '_' + str(date_of_brth).split('-')[2] + \
              '_' + str(date_of_brth).split('-')[1] + \
              '_' + str(date_of_brth).split('-')[0]
        lgn = pytils.translit.translify(lgn)

        login.append(lgn)

        pswd = fake.password(length=8, special_chars=False, digits=True, upper_case=True, lower_case=True)

        if i < NUM_SECTORS:
            status = 'егерь'
        else:
            status = 'охотник'

        line = "{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}|{8}|{9}\n".format(
            lgn,
            pswd,
            surname,
            name,
            patronymic,
            date_of_brth,
            sex_p,
            phone,
            email,
            status
        )

        f.write(line)
        i += 1

    f.close()


def generate_vouchers():
    f = open('vouchers.cvg', 'w')

    for i in range(MAX_AMOUNT + 200):
        duration = choice(range(1, 100))
        amount = choice(range(1, 10))
        prc = 0
        ind = choice(range(1, MAX_AMOUNT))
        id_hunter = hunters[ind]
        id_pricelist = choice(range(1, MAX_AMOUNT))

        line = "{0}|{1}|{2}|{3}|{4}\n".format(
            duration,
            amount,
            prc,
            id_hunter,
            id_pricelist
        )

        f.write(line)
    f.close()


if __name__ == "__main__":
    generate_hunting_grounds()
    generate_sectors()
    generate_price_list()
    generate_accounts()
    generate_huntsmen()
    generate_hunters()
    generate_vouchers()