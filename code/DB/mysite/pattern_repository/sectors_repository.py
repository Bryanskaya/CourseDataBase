from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.sectors import *
from errors.err_sector import *


class SectorsRepository(Repository):
    def create(self, obj: Sector):
        raise NotImplementedError

    def delete(self, obj: Sector):
        raise NotImplementedError

    def update(self, obj_old: Sector, obj_upd: Sector):
        raise NotImplementedError

    def get_all(self) -> [Sector]:
        raise NotImplementedError

    def get_ids(self, id_hunting_ground):
        raise NotImplementedError

    def get_by_id(self, id) -> Sector:
        raise NotImplementedError


class PW_SectorsRepository(SectorsRepository):
    def create(self, obj: Sector):
        try:
            SectorModel.create(id=obj.get_id(),
                               id_husbandry=obj.get_id_husbandry())
        except:
           raise CreateBLObjectSectorErr()

    def delete(self, obj: Sector):
        temp = SectorModel.delete().where(SectorModel.id == obj.id)
        temp.execute()

    # def update(self, obj_old: Sector, obj_upd: Sector):
    #     if self.get_by_id(obj_old.id) is None:
    #         raise IdSectorNotExists()
    #
    #     temp = self.model.update(obj_upd.get_dict()).where(SectorModel.id == obj_upd.id)
    #     try:
    #         temp.execute()
    #     except:
    #         raise UpdateSectorErr()

    def get_all(self) -> [Sector]:
        temp = SectorModel.select()
        return transf_to_objs(temp, Sector)

    def get_ids(self, id_hunting_ground):
        temp = SectorModel.select().where(SectorModel.id_husbandry == id_hunting_ground)
        sectors_set = transf_to_objs(temp, Sector)
        return [x.get_id() for x in sectors_set]

    def get_by_id(self, id) -> Sector:
        temp = SectorModel.select().where(SectorModel.id == id)
        sectors_set = transf_to_objs(temp, Sector)

        if len(sectors_set):
            return sectors_set[0]
        return None
