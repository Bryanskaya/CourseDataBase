from peewee import *
import inject

def get_config_params(to_class, config):
    db_name = config['db_name']
    user = config['db_user']
    pwd = config['db_password']
    host = config['db_host']

    return to_class(db_name, user=user, password=pwd, host=host, autorollback=True)
