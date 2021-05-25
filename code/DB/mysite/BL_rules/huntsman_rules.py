from inject_config import *
from BL_objects.huntsman import *
from errors.err_huntsman import *


class HuntsmanRules(object):
    @staticmethod
    def register(obj: Huntsman):
        huntsman_set = inject.instance(HuntsmanRepository)
        try:
            huntsman_set.create(obj)
        except CreateBLObjectHuntsmanErr:
            obj = None

        return obj