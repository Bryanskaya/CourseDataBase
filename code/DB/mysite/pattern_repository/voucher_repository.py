from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.vouchers import *
from errors.err_voucher import *


class VoucherRepository(Repository):
    def create(self, obj: VoucherModel):
        raise NotImplementedError

    def delete(self, obj: Voucher):
        raise NotImplementedError

    def delete_by_id(self, id):
        raise NotImplementedError

    def update(self, obj_old: Voucher, obj_upd: Voucher):
        raise NotImplementedError

    def get_all(self) -> [Voucher]:
        raise NotImplementedError

    def get_by_id(self, id) -> Voucher:
        raise NotImplementedError


class PW_VoucherRepository(VoucherRepository):
    model = None

    def __init__(self, connection):
        self.model = VoucherModel(connection)

    def create(self, obj: Voucher):
        try:
            self.model.insert(amount_animals=obj.get_amount_animals(),
                                price=obj.get_price(),
                                id_hunter=obj.get_id_hunter(),
                                id_pricelist=obj.get_id_pricelist(),
                                status=obj.get_status()).execute()
        except:
            raise CreateBLObjectVoucherErr()

    def delete(self, obj: Voucher):
        temp = self.model.delete().where(VoucherModel.id == obj.id)
        temp.execute()

    def delete_by_id(self, id):
        temp = self.model.delete().where(VoucherModel.id == id)
        temp.execute()

    def update(self, obj_old: Voucher, obj_upd: Voucher):
        if self.get_by_id(obj_old.id) is None:
            raise IdVoucherNotExists()

        temp = self.model.update(obj_upd.get_dict()).where(VoucherModel.id == obj_upd.id)
        try:
            temp.execute()
        except:
            raise UpdateVoucherErr()

    def get_all(self) -> [Voucher]:
        temp = self.model.select()
        return transf_to_objs(temp, Voucher)

    def get_by_id(self, id) -> Voucher:
        temp = self.model.select().where(VoucherModel.id == id)
        vouchers_set = transf_to_objs(temp, Voucher)

        if len(vouchers_set):
            return vouchers_set[0]
        return None

    def get_by_id_hunter(self, id_hunter) -> Voucher:
        temp = self.model.select().where(VoucherModel.id_hunter == id_hunter)
        vouchers_set = transf_to_objs(temp, Voucher)

        if len(vouchers_set):
            return vouchers_set
        return None