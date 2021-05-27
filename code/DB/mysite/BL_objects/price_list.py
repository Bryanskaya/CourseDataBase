class PriceList(object):
    id = None
    animal = None
    price = None
    is_relevant = None
    id_sector = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.animal = data['animal']
        self.price = data['price']
        self.is_relevant = data['is_relevant']
        self.id_sector = data['id_sector']

    def get_dict(self) -> dict:
        return {'id': self.id,
                'animal': self.animal,
                'price': self.price,
                'is_relevant': self.is_relevant,
                'id_sector': self.id_sector}

    def get_id(self):           return self.id
    def get_animal(self):       return self.animal
    def get_price(self):        return self.price
    def get_is_relevant(self):  return self.is_relevant
    def get_id_sector(self):    return self.id_sector

    def set_id(self, id):               self.id = id
    def set_animal(self, animal):       self.animal = animal
    def set_price(self, price):         self.price = price
    def set_is_relevant(self, mark):    self.is_relevant = mark
    def set_id_sector(self, id):        self.id_sector = id

