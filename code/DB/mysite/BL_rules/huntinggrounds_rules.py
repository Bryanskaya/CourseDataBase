from BL_rules.base_rules import *


class HuntingGroundsRules(BaseRules):
    def get_by_id(self, id):
        grounds_set = inject.instance(HuntingGroundsRepository)(self.connection)
        return grounds_set.get_by_id(id).get_dict()


