class Huntsman(object):
    id = None
    login = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.login = data['login']

    def __ne__(self, other):
        return self.get_dict() != other.get_dict()

    def __eq__(self, other):
        return self.get_dict() == other.get_dict()

    def get_dict(self) -> dict:
        return {'id': self.id,
                'login': self.login}

    def get_id(self):       return self.id
    def get_login(self):    return self.login

    def set_id(self, id):       self.id = id
    def set_login(self, login): self.login = login
