from inject_config import *
from BL_objects.huntsman import *
from errors.err_huntsman import *
from BL_rules.base_rules import *


class HuntsmanRules(BaseRules):
    def register(self, obj: Huntsman):
        huntsman_set = inject.instance(HuntsmanRepository)(self.connection)
        try:
            huntsman_set.create(obj)
        except CreateBLObjectHuntsmanErr:
            obj = None

        return obj

    def get_by_login(self, login):
        huntsman_set = inject.instance(HuntsmanRepository)(self.connection)
        return huntsman_set.get_by_login(login)