from BL_rules.hunter_rules import *
from .base import *
from read_data import *


class HuntingGroundView(BaseView):
    @classmethod
    def get_all(cls):
        return cls.dict_to_str(csv_dict_reader())