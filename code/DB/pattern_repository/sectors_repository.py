from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.sectors import *
from pattern_repository.errors import *


class SectorsRepository(Repository):
    def __init__(self):
        pass


class PW_SectorsRepository(SectorsRepository):
    def __init__(self):
        pass

    def create(self, obj: Sector):
        # try:
        SectorModel.create(id=obj.get_id(),
                           square=obj.get_square(),
                           id_husbandry=obj.get_id_husbandry())

    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = SectorModel.select()

        return transf_to_objs(temp, Sector)
