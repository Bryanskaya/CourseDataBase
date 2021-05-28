from inject_config import *
from BL_objects.hunter import *
from errors.err_hunter import *

from BL_rules.base_rules import *


class HunterRules(BaseRules):
    def register(self, obj: Hunter):
        hunters_set = inject.instance(HunterRepository)(self.connection)

        try:
            hunters_set.create(obj)
        except CreateBLObjectHunterErr:
            obj = None

        return obj