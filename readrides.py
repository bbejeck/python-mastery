import csv
import sys
from collections import namedtuple

Rowt = namedtuple('Rowt', ['route', 'date', 'daytype', 'rides'])


class Row:
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


class Rowslot:
    __slots__ = ['route', 'date', 'daytype', 'rides']

    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as(filename, container='tuple'):
    '''
    Read the bus ride data as a list of tuples
    :param container: container storage type
    :param filename:
    :return: A list of tuples
    '''

    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)
        for row in rows:
            record = put_row_in_container(row, container)
            records.append(record)
        return records


def put_row_in_container(row, container):
    route = row[0]
    date = row[1]
    daytype = row[2]
    rides = int(row[3])
    if container == 'tuple':
        return route, date, daytype, rides
    elif container == 'named_tuple':
        return Rowt(route, date, daytype, rides)
    elif container == 'dict':
        return {
            'route': route,
            'date': date,
            'daytype': daytype,
            'rides': rides
        }
    elif container == 'class':
        return Row(route, date, daytype, rides)
    else:
        return Rowslot(route, date, daytype, rides)


if __name__ == '__main__':
    import tracemalloc
    container = sys.argv[1]
    tracemalloc.start()
    rows = read_rides_as('Data/ctabus.csv', container)
    print(f'Memory Use for container type {container}:  {tracemalloc.get_traced_memory()}')
