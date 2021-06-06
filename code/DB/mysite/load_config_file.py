import json
from errors.err_general import *

class load_config(object):
    filename = None
    data = None

    def __init__(self, fname):
        self.filename = fname

        try:
            f = open(self.filename, 'r')
        except:
            raise OpenFileErr()

        self.data = json.load(f)
        f.close()

    def get_item(self, name):
        if name in self.data.keys():
            return self.data[name]

        return None


class DBConfig(load_config):
    pass

class EmailConfig(load_config):
    def get_smtp_ssl_host(self):
        return self.get_item('smtp_ssl_host')

    def get_smtp_ssl_port(self):
        return self.get_item('smtp_ssl_port')

    def get_username(self):
        return self.get_item('username')

    def get_password(self):
        return self.get_item('password')

    def get_sender(self):
        return self.get_item('sender')

    smtp_ssl_host = property(get_smtp_ssl_host)
    smtp_ssl_port = property(get_smtp_ssl_port)
    username = property(get_username)
    password = property(get_password)
    sender = property(get_sender)
