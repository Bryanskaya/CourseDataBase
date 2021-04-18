from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.hunting_grounds import *
from pattern_repository.errors import *


class HuntingGroundsRepository(Repository):
    def __init__(self):
        pass


class PW_HuntingGroundsRepository(HuntingGroundsRepository):
    def __init__(self):
        pass

    def create(self, obj):
        # try:
        HuntingGroundsModel.create(id=obj.get_id(),
                                   ground_name=obj.get_ground_name(),
                                   square=obj.get_square())

    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = HuntingGroundsModel.select()

        return transf_to_objs(temp, HuntingGrounds)
