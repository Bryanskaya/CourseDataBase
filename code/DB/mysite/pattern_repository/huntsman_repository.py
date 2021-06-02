from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.huntsman import *
from errors.err_huntsman import *


class HuntsmanRepository(Repository):
    def create(self, obj: HuntsmanModel):
        raise NotImplementedError

    def delete(self, obj: Huntsman):
        raise NotImplementedError

    def update(self, obj_old: Huntsman, obj_upd: Huntsman):
        raise NotImplementedError

    def get_all(self) -> [Huntsman]:
        raise NotImplementedError

    def get_by_id(self, id) -> Huntsman:
        raise NotImplementedError

    def get_by_login(self, login) -> Huntsman:
        raise NotImplementedError


class PW_HuntsmanRepository(HuntsmanRepository):
    model = None

    def __init__(self, connection):
        self.model = HuntsmanModel(connection)

    def create(self, obj: Huntsman):
        try:
            self.model.insert(id=obj.get_id(),
                              login=obj.get_login()).execute()
        except:
           raise CreateBLObjectHuntsmanErr()

    def delete(self, obj: Huntsman):
        temp = self.model.delete().where(HuntsmanModel.id == obj.id)
        temp.execute()

    def update(self, obj_old: Huntsman, obj_upd: Huntsman):
        if self.get_by_id(obj_old.id) is None:
            raise IdHuntsmanNotExists()

        temp = self.model.update(obj_upd.get_dict()).where(HuntsmanModel.id == obj_upd.id)
        try:
            temp.execute()
        except:
            raise UpdateHuntsmanErr()

    def get_all(self) -> [Huntsman]:
        temp = self.model.select()
        return transf_to_objs(temp, Huntsman)

    def get_by_id(self, id) -> Huntsman:
        temp = self.model.select().where(HuntsmanModel.id == id)
        huntsman_set = transf_to_objs(temp, Huntsman)

        if len(huntsman_set):
            return huntsman_set[0]
        return None

    def get_by_login(self, login) -> Huntsman:
        temp = self.model.select().where(HuntsmanModel.login == login)
        huntsman_set = transf_to_objs(temp, Huntsman)

        if len(huntsman_set):
            return huntsman_set[0]
        return None
