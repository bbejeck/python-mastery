import csv
import sys
from collections import namedtuple
from collections import Counter
from datetime import datetime
from pprint import pprint

Rowt = namedtuple('Rowt', ['route', 'date', 'daytype', 'rides'])
date_format = '%m/%d/%Y'


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


def find_largest_increase():
    all_rides = read_rides_as('Data/ctabus.csv', 'class')
    first_year = [row for row in all_rides if get_date(row.date).year == 2001]
    year_one_counter = Counter()
    for row in first_year:
        year_one_counter[row.route] += row.rides
    ten_year_counter = Counter()
    ten_years = [row for row in all_rides if filter_by_year(get_date(row.date))]
    for row in ten_years:
        ten_year_counter[row.route] += row.rides
    big_increase = []

    for route, rides in year_one_counter.items():
        big_increase.append((route, ten_year_counter[route] / rides))
    
    sorted_by_increase = sorted(big_increase, key=lambda r: int(r[1]), reverse=True)
    pprint(sorted_by_increase[0:10])


def get_date(dstr):
    return datetime.strptime(dstr, date_format)


def filter_by_year(date):
    return 2001 <= date.year <= 2011


if __name__ == '__main__':
    # import tracemalloc
    #
    # container = sys.argv[1]
    # tracemalloc.start()
    # rows = read_rides_as('Data/ctabus.csv', container)
    # print(f'Memory Use for container type {container}:  {tracemalloc.get_traced_memory()}')
    find_largest_increase()
