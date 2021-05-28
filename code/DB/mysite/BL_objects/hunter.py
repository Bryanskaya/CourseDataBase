class Hunter(object):
    ticket_num = None
    residence = None
    login = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.ticket_num = data['ticket_num']
        self.residence = data['residence']
        self.login = data['login']

    def get_dict(self) -> dict:
        return {'ticket_num': self.ticket_num,
                'residence': self.residence,
                'login': self.login}

    def __ne__(self, other):
        return self.get_dict() != other.get_dict()

    def __eq__(self, other):
        return self.get_dict() == other.get_dict()

    def get_ticket_num(self):   return self.ticket_num
    def get_residence(self):    return self.residence
    def get_login(self):        return self.login

    def set_ticket_num(self, ticket_num):   self.ticket_num = ticket_num
    def set_residence(self, address):       self.residence = address
    def set_login(self, login):             self.login = login
