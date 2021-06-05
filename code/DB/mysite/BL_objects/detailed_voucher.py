class DetailedVoucher(object):
    id_voucher = None
    surname = None
    firstname = None
    patronymic = None
    mobile_phone = None
    animal = None
    amount_animals = None
    ground_name = None
    id_sector = None

    def __init__(self, data):
        if data is None:
            return

        self.id_voucher = data['id_voucher']
        self.surname = data['surname']
        self.firstname = data['firstname']
        self.patronymic = data['patronymic']
        self.mobile_phone = data['mobile_phone']
        self.animal = data['animal']
        self.amount_animals = data['amount_animals']
        self.ground_name = data['ground_name']
        self.id_sector = data['id_sector']

    def get_dict(self) -> dict:
        return {'id_voucher': self.id_voucher,
                'surname': self.surname,
                'firstname': self.firstname,
                'patronymic': self.patronymic,
                'mobile_phone': self.mobile_phone,
                'animal': self.animal,
                'amount_animals': self.amount_animals,
                'ground_name': self.ground_name,
                'id_sector': self.id_sector}

