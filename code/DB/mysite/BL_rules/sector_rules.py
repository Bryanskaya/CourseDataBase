from BL_rules.base_rules import *


class SectorRules(BaseRules):
    def get_ids(self, id_hunting_ground):
        sectors_set = inject.instance(SectorsRepository)(self.connection)
        return sectors_set.get_ids(id_hunting_ground)
