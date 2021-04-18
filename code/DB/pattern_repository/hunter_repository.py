from pattern_repository.repository import *
from pattern_repository.peewee_models import *
from BL_objects.hunter import *
from pattern_repository.errors import *


class HunterRepository(Repository):
    def __init__(self):
        pass


class PW_HunterRepository(HunterRepository):
    def __init__(self):
        pass

    def create(self, obj):
        #try:
            HunterModel.create(ticket_num=obj.get_ticket_num(),
                          surname=obj.get_surname(),
                          firstname=obj.get_firstname(),
                          patronymic=obj.get_patronymic(),
                          date_of_birth=obj.get_date_of_birth(),
                          sex=obj.get_sex(),
                          residence=obj.get_residence(),
                          mobile_phone=obj.get_mobile_phone(),
                          email=obj.get_email(),
                          login=obj.get_login())
        #except:
        #    return CreareBLObjectError


    def get(self):
        temp = HunterModel.select()

        return transf_to_objs(temp, Hunter)
