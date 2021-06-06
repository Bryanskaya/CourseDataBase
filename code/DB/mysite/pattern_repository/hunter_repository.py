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

    def get_by_ticket_num(self, ticket_num) -> Hunter:
        raise NotImplementedError

    def get_by_login(self, login) -> Hunter:
        raise NotImplementedError


class PW_HunterRepository(HunterRepository):
    model = None

    def __init__(self, connection):
        self.model = HunterModel(connection)

    def create(self, obj: Hunter):
        try:
            self.model.insert(ticket_num=obj.get_ticket_num(),
                              residence=obj.get_residence(),
                              login=obj.get_login()).execute()
        except:
            raise CreateBLObjectHunterErr()

    def delete(self, obj: Hunter):
        temp = self.model.delete().where(HunterModel.ticket_num == obj.ticket_num)
        temp.execute()

    def delete_by_huntsman(self, ticket_num):
        temp = self.model.delete().where(HunterModel.ticket_num == ticket_num)
        temp.execute()

    def update(self, obj_old: Hunter, obj_upd: Hunter):
        if self.get_by_ticket_num(obj_old.ticket_num) is None:
            raise LoginHunterNotExists()

        temp = self.model.update(obj_upd.get_dict()).where(HunterModel.ticket_num == obj_upd.ticket_num)
        try:
            temp.execute()
        except:
            raise UpdateHunterErr()

    def get_all(self) -> [Hunter]:
        temp = self.model.select()
        return transf_to_objs(temp, Hunter)

    def get_by_ticket_num(self, ticket_num: str) -> Hunter:
        temp = self.model.select().where(HunterModel.ticket_num == ticket_num)
        hunters_set = transf_to_objs(temp, Hunter)

        if len(hunters_set):
            return hunters_set[0]
        return None

    def get_by_login(self, login) -> Hunter:
        temp = self.model.select().where(HunterModel.login == login)
        hunters_set = transf_to_objs(temp, Hunter)

        if len(hunters_set):
            return hunters_set[0]
        return None


