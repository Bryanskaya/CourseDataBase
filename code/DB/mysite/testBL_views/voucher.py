from BL_rules.voucher_rules import *
from .base import *

class VoucherView(BaseView):
    @classmethod
    def cur_vouchers(cls, login):
        voucher_rules = VoucherRules('admin')

        try:
            vouchers, requests = voucher_rules.get_by_login(login)
        except LoginNotExists:
            return "ОШИБКА: такого логина нет в БД", ""

        if vouchers is None:
            return "Путёвок нет", ""

        return cls.set_to_str(vouchers), cls.set_to_str(requests)