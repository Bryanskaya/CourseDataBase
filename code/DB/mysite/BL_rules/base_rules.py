from inject_config import *
from errors.err_account import *

class BaseRules(object):
    connection = None

    def __init__(self, role, connection=None):
        if connection is not None:
            self.connection = connection
            return

        self.connection = inject.instance(CurConnection) #TODO change to role connection

        if role == 'admin' or role == 'админ':
            self.connection = inject.instance(AdminConnection)
        elif role == 'hunter' or role == 'охотник':
            self.connection = inject.instance(HunterConnection)
        elif role == 'huntsman' or role == 'егерь':
            self.connection = inject.instance(HuntsmanConnection)

    def to_dict(self, data):
        res = {}
        for key in data.keys():
            res[key] = data[key]

        return res