import csv

FILENAME = '../../SQL_files/generator/hunting_grounds_real.csv'


def csv_dict_reader(filename=FILENAME):
    grounds = {}
    i = 1

    f = open(filename)
    reader = csv.DictReader(f)
    for line in reader:
        grounds[str(line['Субъект'])] = i
        i += 1

    return grounds


