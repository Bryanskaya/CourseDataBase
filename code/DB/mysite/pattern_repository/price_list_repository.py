from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.price_list import *
from errors.err_price_list import *


class PriceListRepository(Repository):
    def create(self, obj: PriceListModel):
        raise NotImplementedError

    def delete(self, obj: PriceList):
        raise NotImplementedError

    def update(self, obj_old: PriceList, obj_upd: PriceList):
        raise NotImplementedError

    def get_all(self) -> [PriceList]:
        raise NotImplementedError

    def get_by_id(self, id) -> PriceList:
        raise NotImplementedError


class PW_PriceListRepository(PriceListRepository):
    model = None

    def __init__(self, connection):
        self.model = PriceListModel(connection)

    def create(self, obj: PriceList):
        try:
            self.model.insert(id=obj.get_id(),
                              animal=obj.get_animal(),
                              price=obj.get_price(),
                              is_relevant=obj.get_is_relevant(),
                              id_sector=obj.get_id_sector()).execute()
        except:
           raise CreateBLObjectPriceListErr()

    def delete(self, obj: PriceList):
        temp = self.model.delete().where(PriceListModel.id == obj.id)
        temp.execute()

    def update(self, obj_old: PriceList, obj_upd: PriceList):
        if self.get_by_id(obj_old.id) is None:
            raise IdPriceListNotExists()

        temp = self.model.update(obj_upd.get_dict()).where(PriceListModel.id == obj_upd.id)
        try:
            temp.execute()
        except:
            raise UpdatePriceListErr()

    def get_all(self) -> [PriceList]:
        temp = self.model.select()
        return transf_to_objs(temp, PriceList)

    def get_by_id(self, id) -> PriceList:
        temp = self.model.select().where(PriceListModel.id == id)
        list_set = transf_to_objs(temp, PriceList)

        if len(list_set):
            return list_set[0]
        return None
