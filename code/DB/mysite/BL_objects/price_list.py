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

    def get_id(self):   return self.id

    def get_animal(self):    return self.animal

    def get_price(self):    return self.price

    def get_is_relevant(self):        return self.is_relevant

    def get_id_sector(self):        return self.id_sector
