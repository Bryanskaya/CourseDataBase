from pattern_repository.repository import *
from BL_objects.detailed_voucher import *


def get_requests_all(connection, func_name):
    cursor = connection.cursor()
    cursor.callproc(func_name)

    res = []
    for obj in cursor.fetchall():
        obj_dict = {}
        for col, val in zip(cursor.description, obj):
            column_name = col[0]
            obj_dict[column_name] = val
        res.append(obj_dict)
    cursor.close()

    return res


def dicts_to_objs(dict_arr, obj_class):
    obj_arr = []
    for obj_dict in dict_arr:
        obj_arr.append(obj_class(obj_dict))

    return obj_arr


class DetailedVoucherRepository(Repository):
    def get_requests_all(self):
        raise NotImplementedError

    def get_vouchers_all(self):
        raise NotImplementedError

class PW_DetailedRepository(DetailedVoucherRepository):
    connection = None

    def __init__(self, connection):
        self.connection = connection

    def get_requests_all(self):
        res = get_requests_all(self.connection, 'ShowAllRequests')
        return dicts_to_objs(res, DetailedVoucher)

    def get_vouchers_all(self):
        res = get_requests_all(self.connection, 'ShowAllVouchers')
        return dicts_to_objs(res, DetailedVoucher)