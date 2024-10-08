import peewee

from mysite.pattern_repository.db_config import *
from mysite.load_config_file import *


def init_injector(bnd):
    bnd.bind(peewee.Database, peewee.PostgresqlDatabase)
    bnd.bind_to_constructor(load_config,
                            lambda: load_config('config.json'))
    bnd.bind_to_constructor(CurConnection,
                            lambda: get_config_params(inject.instance(peewee.Database), inject.instance(load_config)))


inject.configure(init_injector)

from mysite.pattern_repository.hunter_repository import *
from mysite.pattern_repository.hunting_grounds_repository import *
from mysite.pattern_repository.sectors_repository import *
from mysite.pattern_repository.accounts_repository import *
from mysite.pattern_repository.huntsman_repository import *
from mysite.pattern_repository.price_list_repository import *
from mysite.pattern_repository.voucher_repository import *


def injector(bnd):
    init_injector(bnd)

    bnd.bind_to_constructor(HunterRepository, lambda: PW_HunterRepository())
    bnd.bind_to_constructor(HuntingGroundsRepository, lambda: PW_HuntingGroundsRepository())
    bnd.bind_to_constructor(SectorsRepository, lambda: PW_SectorsRepository())
    bnd.bind_to_constructor(AccountsRepository, lambda: PW_AccountsRepository())
    bnd.bind_to_constructor(HuntsmanRepository, lambda: PW_HuntsmanRepository())
    bnd.bind_to_constructor(PriceListRepository, lambda: PW_PriceListRepository())
    bnd.bind_to_constructor(VoucherRepository, lambda: PW_VoucherRepository())


inject.clear_and_configure(injector)


def main():
    hunter = inject.instance(HunterRepository)
    print(hunter)


if __name__ == "__main__":
    main()
