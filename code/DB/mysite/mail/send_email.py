from errors.err_general import *
import json

class SendMail():
    filename = None
    data = None

    smtp_ssl_host = None
    smtp_ssl_port = None
    username = None
    password = None
    sender = None
    targets = []

    def __init__(self, fname, target):
        self.filename = fname

        try:
            f = open(self.filename, 'r')
        except:
            raise OpenFileErr()

        self.data = json.load(f)
        f.close()