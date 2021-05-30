import peewee

from pattern_repository.db_config import *
from pattern_repository.repository import * #for CurConnection
from load_config_file import *


def init_injector(bnd):
    bnd.bind(peewee.Database, peewee.PostgresqlDatabase)
    bnd.bind_to_constructor(load_config, lambda: load_config('config.json'))
    bnd.bind_to_constructor(CurConnection, lambda: get_config_params(inject.instance(peewee.Database),
                                                                     inject.instance(load_config).get_item('admin_connection')))

    bnd.bind_to_constructor(AdminConnection, lambda: get_config_params(inject.instance(peewee.Database),
                                                                       inject.instance(load_config).get_item('admin_connection')))
    bnd.bind_to_constructor(HunterConnection, lambda: get_config_params(inject.instance(peewee.Database),
                                                                        inject.instance(load_config).get_item('hunter_connection')))
    bnd.bind_to_constructor(HuntsmanConnection, lambda: get_config_params(inject.instance(peewee.Database),
                                                                          inject.instance(load_config).get_item('huntsman_connection')))


inject.clear_and_configure(init_injector)

from pattern_repository.hunter_repository import HunterRepository, PW_HunterRepository
from pattern_repository.hunting_grounds_repository import *
from pattern_repository.sectors_repository import *
from pattern_repository.accounts_repository import *
from pattern_repository.huntsman_repository import *
from pattern_repository.price_list_repository import *
from pattern_repository.voucher_repository import *



def injector(bnd):
    init_injector(bnd)

    bnd.bind(HunterRepository, PW_HunterRepository)
    bnd.bind(HuntingGroundsRepository, PW_HuntingGroundsRepository)
    bnd.bind(SectorsRepository, PW_SectorsRepository)
    bnd.bind(AccountsRepository, PW_AccountsRepository)
    bnd.bind(HuntsmanRepository, PW_HuntsmanRepository)
    bnd.bind(PriceListRepository, PW_PriceListRepository)
    bnd.bind(VoucherRepository, PW_VoucherRepository)


inject.clear_and_configure(injector)
