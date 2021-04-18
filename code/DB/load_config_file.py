import json


class load_config(object):
    filename = None
    data = None

    def __init__(self, fname):
        self.filename = fname

        f = open(self.filename, 'r')
        self.data = json.load(f)
        f.close()

    def get_item(self, name):
        if name in self.data.keys():
            return self.data[name]

        return None
