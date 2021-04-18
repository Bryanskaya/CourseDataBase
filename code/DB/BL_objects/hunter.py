class Hunter(object):
    ticket_num = None
    surname = None
    firstname = None
    patronymic = None
    date_of_birth = None
    sex = None
    residence = None
    mobile_phone = None
    email = None
    login = None

    def __init__(self, data):   #**
        if data is None:
            return

        self.ticket_num = data['ticket_num']
        self.surname = data['surname']
        self.firstname = data['firstname']
        self.patronymic = data['patronymic']
        self.date_of_birth = data['date_of_birth']
        self.sex = data['sex']
        self.residence = data['residence']
        self.mobile_phone = data['mobile_phone']
        self.email = data['email']
        self.login = data['login']


    def get_ticket_num(self):       return self.ticket_num
    def get_surname(self):          return self.surname
    def get_firstname(self):        return self.firstname
    def get_patronymic(self):       return self.patronymic
    def get_date_of_birth(self):    return self.date_of_birth
    def get_sex(self):              return self.sex
    def get_residence(self):        return self.residence
    def get_mobile_phone(self):     return self.mobile_phone
    def get_email(self):            return self.email
    def get_login(self):            return self.login