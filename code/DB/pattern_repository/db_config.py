def get_config_params(to_class, config):
    db_name = config.get_item('db_name')
    user = config.get_item('db_user')
    pwd = config.get_item('db_password')
    host = config.get_item('db_host')

    return to_class(db_name, user=user, password=pwd, host=host)
