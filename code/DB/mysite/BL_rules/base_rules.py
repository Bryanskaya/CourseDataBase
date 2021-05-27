from inject_config import *
from errors.err_account import *

class BaseRules(object):
    connection = None

    def __init__(self, role):
        self.connection = inject.instance(CurConnection) #TODO change to role connection