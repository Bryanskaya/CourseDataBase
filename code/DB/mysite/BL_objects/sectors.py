class Sector(object):
    id = None
    id_husbandry = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.id_husbandry = data['id_husbandry']

    def get_id(self):           return self.id

    def get_id_husbandry(self): return self.id_husbandry
