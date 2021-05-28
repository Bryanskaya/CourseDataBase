from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.vouchers import *
from errors.err_voucher import *


class VoucherRepository(Repository):
    def create(self, obj: VoucherModel):
        raise NotImplementedError

    def delete(self, obj: Voucher):
        raise NotImplementedError

    def update(self, obj_old: Voucher, obj_upd: Voucher):
        raise NotImplementedError

    def get_all(self) -> [Voucher]:
        raise NotImplementedError

    def get_by_id(self, id) -> Voucher:
        raise NotImplementedError


class PW_VoucherRepository(VoucherRepository):
    def __init__(self):
        pass

    def create(self, obj: VoucherModel):
        try:
            VoucherModel.create(id=obj.get_id(),
                                duration_days=obj.get_duration_days(),
                                amount_animals=obj.get_amount_animals(),
                                price=obj.get_price(),
                                id_hunter=obj.get_id_hunter(),
                                id_pricelist=obj.get_id_pricelist())
        except:
           raise CreateBLObjectVoucherErr()

    def delete(self, obj: Voucher):
        temp = VoucherModel.delete().where(VoucherModel.id == obj.id)
        temp.execute()

    # def update(self, obj_old: Voucher, obj_upd: Voucher):
    #     if self.get_by_id(obj_old.id) is None:
    #         raise IdVoucherNotExists()
    #
    #     temp = self.model.update(obj_upd.get_dict()).where(VoucherModel.id == obj_upd.id)
    #     try:
    #         temp.execute()
    #     except:
    #         raise UpdateVoucherErr()

    def get_all(self) -> [Voucher]:
        temp = VoucherModel.select()
        return transf_to_objs(temp, Voucher)

    def get_by_id(self, id) -> Voucher:
        temp = VoucherModel.select().where(VoucherModel.id == id)
        vouchers_set = transf_to_objs(temp, Voucher)

        if len(vouchers_set):
            return vouchers_set[0]
        return None