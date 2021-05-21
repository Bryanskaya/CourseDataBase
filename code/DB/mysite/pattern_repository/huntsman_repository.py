from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.huntsman import *


class HuntsmanRepository(Repository):
    def __init__(self):
        pass


class PW_HuntsmanRepository(HuntsmanRepository):
    def __init__(self):
        pass

    def create(self, obj: HuntsmanModel):
        # try:
        HuntsmanModel.create(id=obj.get_id(),
                             login=obj.get_login())
    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = HuntsmanModel.select()

        return transf_to_objs(temp, Huntsman)
