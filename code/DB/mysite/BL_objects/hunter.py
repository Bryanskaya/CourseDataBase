class Hunter(object):
    ticket_num = None
    address = None
    login = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.ticket_num = data['ticket_num']
        self.address = data['address']
        self.login = data['login']

    def get_dict(self) -> dict:
        return {'ticket_num': self.ticket_num,
                'residence': self.address,
                'login': self.login}

    def get_ticket_num(self):   return self.ticket_num
    def get_address(self):    return self.address
    def get_login(self):        return self.login

    def set_ticket_num(self, ticket_num):   self.ticket_num = ticket_num
    def set_address(self, address):         self.address = address
    def set_login(self, login):             self.login = login
