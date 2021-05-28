class Voucher(object):
    id = None
    duration_days = None
    amount_animals = None
    price = None
    id_hunter = None
    id_pricelist = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.duration_days = data['duration_days']
        self.amount_animals = data['amount_animals']
        self.price = data['price']
        self.id_hunter = data['id_hunter']
        self.id_pricelist = data['id_pricelist']

    def get_dict(self) -> dict:
        return {'id': self.id,
                'duration_days': self.duration_days,
                'amount_animals': self.amount_animals,
                'price': self.price,
                'id_hunter': self.id_hunter,
                'id_pricelist': self.id_pricelist}

    def get_id(self):               return self.id
    def get_duration_days(self):    return self.duration_days
    def get_amount_animals(self):   return self.amount_animals
    def get_price(self):            return self.price
    def get_id_hunter(self):        return self.id_hunter
    def get_id_pricelist(self):     return self.id_pricelist

    def set_id(self, id):               self.id = id
    def set_duration_days(self, num):   self.duration_days = num
    def set_amount_animals(self, num):  self.amount_animals = num
    def set_price(self, price):         self.price = price
    def set_id_hunter(self, id):        self.id_hunter = id
    def set_id_pricelist(self, id):     self.id_pricelist = id

