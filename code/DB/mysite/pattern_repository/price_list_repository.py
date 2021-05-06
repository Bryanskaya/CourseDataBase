from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.price_list import *


class PriceListRepository(Repository):
    def __init__(self):
        pass


class PW_PriceListRepository(PriceListRepository):
    def __init__(self):
        pass

    def create(self, obj: PriceListModel):
        # try:
        PriceListModel.create(id=obj.get_id(),
                              animal=obj.get_animal(),
                              price=obj.get_price(),
                              is_relevant=obj.get_is_relevant(),
                              id_sector=obj.get_id_sector())
    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = PriceListModel.select()

        return transf_to_objs(temp, PriceList)
