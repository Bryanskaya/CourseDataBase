class Voucher(object):
    id = None
    amount_animals = None
    price = None
    id_hunter = None
    id_pricelist = None
    status = None

    def __init__(self, data):  # **
        if data is None:
            return

        if 'id' in data.keys():
            self.id = data['id']
        self.amount_animals = data['amount_animals']
        self.price = data['price']
        self.id_hunter = data['id_hunter']
        self.id_pricelist = data['id_pricelist']
        self.status = data['status']

    def get_dict(self) -> dict:
        return {'id': self.id,
                'amount_animals': self.amount_animals,
                'price': self.price,
                'id_hunter': self.id_hunter,
                'id_pricelist': self.id_pricelist,
                'status': self.status}

    def __ne__(self, other):
        return self.get_dict() != other.get_dict()

    def __eq__(self, other):
        return self.get_dict() == other.get_dict()

    def get_id(self):               return self.id
    def get_amount_animals(self):   return self.amount_animals
    def get_price(self):            return self.price
    def get_id_hunter(self):        return self.id_hunter
    def get_id_pricelist(self):     return self.id_pricelist
    def get_status(self):           return self.status

    def set_id(self, id):               self.id = id
    def set_amount_animals(self, num):  self.amount_animals = num
    def set_price(self, price):         self.price = price
    def set_id_hunter(self, id):        self.id_hunter = id
    def set_id_pricelist(self, id):     self.id_pricelist = id
    def set_status(self, status):       self.status = status

