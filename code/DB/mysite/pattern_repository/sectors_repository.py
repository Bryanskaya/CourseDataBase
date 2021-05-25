from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.sectors import *
from errors.err_sector import *


class SectorsRepository(Repository):
    def create(self, obj: Sector):
        raise NotImplementedError

    def delete(self, obj: Sector):
        raise NotImplementedError

    def get_all(self) -> [Sector]:
        raise NotImplementedError

    def get_ids(self, id_hunting_ground):
        raise NotImplementedError


class PW_SectorsRepository(SectorsRepository):
    def create(self, obj: Sector):
        try:
            SectorModel.create(id=obj.get_id(),
                               id_husbandry=obj.get_id_husbandry())
        except:
           raise CreateBLObjectSectorErr()

    def get(self):
        temp = SectorModel.select()
        return transf_to_objs(temp, Sector)

    def get_ids(self, id_hunting_ground):
        temp = SectorModel.select().where(SectorModel.id_husbandry == id_hunting_ground)
        sectors_set = transf_to_objs(temp, Sector)
        return [x.get_id() for x in sectors_set]
