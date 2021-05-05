from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.hunter import *
from pattern_repository.errors import *

class HunterRepository(Repository):
    def __init__(self):
        pass


class PW_HunterRepository(HunterRepository):
    def __init__(self):
        pass

    def create(self, obj: HunterModel):
        # try:
        HunterModel.create(ticket_num=obj.get_ticket_num(),
                           residence=obj.get_residence(),
                           login=obj.get_login())
    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = HunterModel.select()

        return transf_to_objs(temp, Hunter)
