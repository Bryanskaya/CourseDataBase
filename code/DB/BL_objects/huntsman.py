class Huntsman(object):
    id = None
    experience = None
    salary = None
    login = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.experience = data['experience']
        self.salary = data['salary']
        self.login = data['login']

    def get_id(self):   return self.id

    def get_experience(self):    return self.experience

    def get_salary(self):    return self.salary

    def get_login(self):        return self.login
