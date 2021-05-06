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

    def get_ticket_num(self):   return self.ticket_num

    def get_residence(self):    return self.residence

    def get_login(self):        return self.login
