import inject
from pattern_repository import rps


def injector(binder):
#    binder.install(my_config2)  # Импортируем другую конфигурацию
#    binder.bind(Db, RedisDb('localhost:1234'))
#    binder.bind_to_provider(CurrentUser, get_current_user)
    binder.bind_to_constructor(Cache, lambda: RedisCache(address='localhost:1234'))
    binder.bind("database", )




inject.configure(my_config)

def main():
    pass

if __name__ == "__main__":
    main()