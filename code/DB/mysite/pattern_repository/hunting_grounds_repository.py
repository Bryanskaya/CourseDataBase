from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.hunting_grounds import *
from errors.err_hunting_ground import *


class HuntingGroundsRepository(Repository):
    def create(self, obj: HuntingGrounds):
        raise NotImplementedError

    def delete(self, obj: HuntingGrounds):
        raise NotImplementedError

    def update(self, obj_old: HuntingGrounds, obj_upd: HuntingGrounds):
        raise NotImplementedError

    def get_all(self) -> [HuntingGrounds]:
        raise NotImplementedError

    def get_by_id(self, id) -> HuntingGrounds:
        raise NotImplementedError


class PW_HuntingGroundsRepository(HuntingGroundsRepository):
    model = None

    def __init__(self, connection):
        self.model = HuntingGroundsModel(connection)

    def create(self, obj: HuntingGrounds):
        try:
            self.model.insert(id=obj.get_id(),
                              ground_name=obj.get_ground_name()).execute()
        except:
           raise CreareBLObjectHuntGroundError()

    def delete(self, obj: HuntingGrounds):
        temp = self.model.delete().where(HuntingGroundsModel.id == obj.id)
        temp.execute()

    def update(self, obj_old: HuntingGrounds, obj_upd: HuntingGrounds):
        if self.get_by_id(obj_old.id) is None:
            raise IdHuntGroundNotExists()

        temp = self.model.update(obj_upd.get_dict()).where(HuntingGroundsModel.id == obj_upd.id)
        try:
            temp.execute()
        except:
            raise UpdateHuntGroundErr()

    def get_all(self) -> [HuntingGrounds]:
        temp = self.model.select()
        return transf_to_objs(temp, HuntingGrounds)

    def get_by_id(self, id) -> HuntingGrounds:
        temp = self.model.select().where(HuntingGroundsModel.id == id)
        huntground_set = transf_to_objs(temp, HuntingGrounds)

        if len(huntground_set):
            return huntground_set[0]
        return None
