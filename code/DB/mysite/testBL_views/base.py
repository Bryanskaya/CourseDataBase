from prettytable import PrettyTable

class BaseView(object):
    @classmethod
    def set_to_str(cls, set: [dict]):
        if not len(set):
            return 'Not found'

        title = list(set[0].keys())
        values = []

        table = PrettyTable(title)

        for elem in set:
            for key, value in elem.items():
                values.append(value)

        while values:
            table.add_row(values[:len(title)])
            values = values[len(title):]

        return str(table)


    @classmethod
    def dict_to_str(cls, data: dict):
        if not len(data):
            return 'Not found'

        title = []
        values = []

        table = PrettyTable(title)

        for item in data.items():
            values.append(item)

        for i in values:
            table.add_row(i)

        return str(table)