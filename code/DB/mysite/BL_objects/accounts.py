class Account(object):
    login = None
    salt = None
    hashed_password = None
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
        self.salt = data['salt']
        self.hashed_password = data['hashed_password']
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
                'salt': self.salt,
                'hashed_password': self.hashed_password,
                'surname': self.surname,
                'firstname': self.firstname,
                'patronymic': self.patronymic,
                'date_of_birth': self.date_of_birth,
                'sex': self.sex,
                'mobile_phone': self.mobile_phone,
                'email': self.email,
                'type_role': self.type_role}

    def __ne__(self, other):
        return self.get_dict() != other.get_dict()

    def __eq__(self, other):
        return self.get_dict() == other.get_dict()

    def get_login(self):            return self.login
    def get_salt(self):             return self.salt
    def get_hashed_password(self):  return self.hashed_password
    def get_surname(self):          return self.surname
    def get_firstname(self):        return self.firstname
    def get_patronymic(self):       return self.patronymic
    def get_date_of_birth(self):    return self.date_of_birth
    def get_sex(self):              return self.sex
    def get_mobile_phone(self):     return self.mobile_phone
    def get_email(self):            return self.email
    def get_type_role(self):        return self.type_role

    def set_login(self, login):                     self.login = login
    def set_salt(self, salt):                       self.salt = salt
    def set_hashed_password(self, hashed_password): self.hashed_password = hashed_password
    def set_surname(self, surname):                 self.surname = surname
    def set_firstname(self, firstname):             self.firstname = firstname
    def set_patronymic(self, patronymic):           self.patronymic = patronymic
    def set_date_of_birth(self, date):              self.date_of_birth = date
    def set_sex(self, sex):                         self.sex = sex
    def set_mobile_phone(self, phone):              self.mobile_phone = phone
    def set_email(self, email):                     self.email = email
    def set_type_role(self, role):                  self.type_role = role
