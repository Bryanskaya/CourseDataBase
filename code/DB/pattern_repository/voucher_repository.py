from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.vouchers import *
from pattern_repository.errors import *


class VoucherRepository(Repository):
    def __init__(self):
        pass


class PW_VoucherRepository(VoucherRepository):
    def __init__(self):
        pass

    def create(self, obj: VoucherModel):
        # try:
        VoucherModel.create(id=obj.get_id(),
                            duration_days=obj.get_duration_days(),
                            amount_animals=obj.get_amount_animals(),
                            price=obj.get_price(),
                            id_hunter=obj.get_id_hunter(),
                            id_pricelist=obj.get_id_pricelist())

    # except:
    #    return CreareBLObjectError

    def get(self):
        temp = VoucherModel.select()

        return transf_to_objs(temp, Voucher)
