class Repository(object):
    def __init__(self):
        pass

    def create(self, obj):
        raise NotImplementedError

    def delete(self, obj):
        raise NotImplementedError

    def get(self):
        raise NotImplementedError

    def update(self, obj):
        raise NotImplementedError


class CurConnection(object):
    pass
