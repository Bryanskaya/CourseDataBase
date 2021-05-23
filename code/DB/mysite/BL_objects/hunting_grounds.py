class HuntingGrounds(object):
    id = None
    ground_name = None

    def __init__(self, data):  # **
        if data is None:
            return

        self.id = data['id']
        self.ground_name = data['ground_name']

    def get_id(self):           return self.id

    def get_ground_name(self):  return self.ground_name
