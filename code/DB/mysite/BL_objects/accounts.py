class Account(object):
    login = None
    pswd = None
    surname = None
    firstname = None
    patronymic = None
    date_of_birth = None
    sex = None
    mobile_phone = None
    email = None
    type_role = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.login = data['login']
        self.pswd = data['pswd']
        self.surname = data['surname']
        self.firstname = data['firstname']
        self.patronymic = data['patronymic']
        self.date_of_birth = data['date_of_birth']
        self.sex = data['sex']
        self.mobile_phone = data['mobile_phone']
        self.email = data['email']
        self.type_role = data['type_role']

    def get_dict(self) -> dict:
        return {'login': self.login,
                'password': self.pswd,
                'surname': self.surname,
                'firstname': self.firstname,
                'patronymic': self.patronymic,
                'date_of_birth': self.date_of_birth,
                'sex': self.sex,
                'mobile_phone': self.mobile_phone,
                'email': self.email,
                'type_role': self.type_role}

    def get_login(self):            return self.login

    def get_password(self):         return self.pswd

    def get_surname(self):          return self.surname

    def get_firstname(self):        return self.firstname

    def get_patronymic(self):       return self.patronymic

    def get_date_of_birth(self):    return self.date_of_birth

    def get_sex(self):              return self.sex

    def get_mobile_phone(self):     return self.mobile_phone

    def get_email(self):            return self.email

    def get_type_role(self):        return self.type_role
