class Huntsman(object):
    id = None
    login = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.login = data['login']

    def get_id(self):   return self.id

    def get_login(self):        return self.login
