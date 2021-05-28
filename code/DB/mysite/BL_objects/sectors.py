class Sector(object):
    id = None
    id_husbandry = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.id_husbandry = data['id_husbandry']

    def get_dict(self) -> dict:
        return {'id': self.id,
                'id_husbandry': self.id_husbandry}

    def get_id(self):           return self.id
    def get_id_husbandry(self): return self.id_husbandry

    def set_id(self, id):           self.id = id
    def set_id_husbandry(self, id): self.id_husbandry = id
