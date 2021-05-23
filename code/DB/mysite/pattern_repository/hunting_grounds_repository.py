from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.hunting_grounds import *


class HuntingGroundsRepository(Repository):
    def __init__(self):
        pass


class PW_HuntingGroundsRepository(HuntingGroundsRepository):
    def __init__(self):
        pass

    def create(self, obj: HuntingGrounds):
        # try:
        HuntingGroundsModel.create(id=obj.get_id(),
                                   ground_name=obj.get_ground_name())

    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = HuntingGroundsModel.select()

        return transf_to_objs(temp, HuntingGrounds)
