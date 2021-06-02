from BL_rules.huntsman_rules import *
from .base import *

class HuntsmanView(BaseView):
    @classmethod
    def get_all(cls):
        huntsman_rules = HuntsmanRules('admin')
        res = huntsman_rules.get_all_detailed()
        return cls.set_to_str(res)