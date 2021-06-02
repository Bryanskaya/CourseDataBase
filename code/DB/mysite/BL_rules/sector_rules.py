from BL_rules.base_rules import *


class SectorRules(BaseRules):
    def get_by_id(self, id):
        sectors_set = inject.instance(SectorsRepository)(self.connection)
        return sectors_set.get_by_id(id)

    def get_ids(self, id_hunting_ground):
        sectors_set = inject.instance(SectorsRepository)(self.connection)
        return sectors_set.get_ids(id_hunting_ground)

    def get_id_husbandry(self, id):
        sectors_set = inject.instance(SectorsRepository)(self.connection)
        return sectors_set.get_by_id(id).get_dict()


