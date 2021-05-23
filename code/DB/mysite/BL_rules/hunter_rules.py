from inject_config import *
from BL_objects.hunter import *
from errors.err_account import *


class HunterRules(object):
    @staticmethod
    def register(obj: Hunter):
        hunters_set = inject.instance(HunterRepository)
        try:
            hunters_set.create(obj)
        except CreateBLObjectHunterErr:
            obj = None

        return obj