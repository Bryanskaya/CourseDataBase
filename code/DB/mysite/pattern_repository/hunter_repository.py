from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.hunter import *
from errors.err_hunter import *


class HunterRepository(Repository):
    def create(self, obj: Hunter):
        raise NotImplementedError

    def delete(self, obj: Hunter):
        raise NotImplementedError

    def update(self, obj_old: Hunter, obj_upd: Hunter):
        raise NotImplementedError

    def get_all(self) -> [Hunter]:
        raise NotImplementedError

    def get_by_login(self, login) -> Hunter:
        raise NotImplementedError


class PW_HunterRepository(HunterRepository):
    def create(self, obj: HunterModel):
        try:
            HunterModel.create(ticket_num=obj.get_ticket_num(),
                               residence=obj.get_address(),
                               login=obj.get_login())
        except:
            raise CreateBLObjectHunterErr()

    def delete(self, obj: Hunter):
        temp = HunterModel.delete().where(HunterModel.login == obj.login)
        temp.execute()

    # def update(self, obj_old: Hunter, obj_upd: Hunter):
    #     if self.get_by_login(obj_old.login) is None:
    #         raise LoginHunterNotExists()
    #
    #     temp = self.model.update(obj_upd.get_dict()).where(HunterModel.login == obj_upd.login)
    #     try:
    #         temp.execute()
    #     except:
    #         raise UpdateHunterErr()

    def get_all(self) -> [Hunter]:
        temp = HunterModel.select()
        return transf_to_objs(temp, Hunter)

    def get_by_login(self, login: str) -> Hunter:
        temp = HunterModel.select().where(HunterModel.login == login)
        hunters_set = transf_to_objs(temp, Hunter)

        if len(hunters_set):
            return hunters_set[0]
        return None
