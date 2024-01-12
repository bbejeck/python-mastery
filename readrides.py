import collections.abc
import csv
from collections import namedtuple
from collections import Counter
from datetime import datetime
from pprint import pprint

Rowt = namedtuple('Rowt', ['route', 'date', 'daytype', 'rides'])
date_format = '%m/%d/%Y'


class RideData(collections.abc.Sequence):
    def __init__(self):
        self.routes = []
        self.dates = []
        self.daytypes = []
        self.numrides = []

    def __len__(self):
        return len(self.routes)

    def __getitem__(self, index):
        if type(index) is slice:
            print(f'returning from slice {index}')
            ride_data_slice = RideData()
            sl_routes = self.routes[index]
            sl_date = self.dates[index]
            sl_daytype = self.daytypes[index]
            sl_rides = self.numrides[index]
            for route, date, dt, rides in zip(sl_routes, sl_date, sl_daytype, sl_rides):
                ride_data_slice.append({'route': route, 'date': date, 'daytype': dt, 'rides': rides})
            return ride_data_slice
        else:
            print(f'returning value at index {index}')
            return {
                'route': self.routes[index],
                'date': self.dates[index],
                'daytype': self.daytypes[index],
                'rides': self.numrides[index]
             }

    def append(self, d):
        self.routes.append(d['route'])
        self.dates.append(d['date'])
        self.daytypes.append(d['daytype'])
        self.numrides.append(d['rides'])


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


def read_rides_as(filename, container='dict'):
    '''
    Read the bus ride data as a list of tuples
    :param container: container storage type
    :param filename:
    :return: A list of tuples
    '''

    records = RideData()
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
    import tracemalloc

    # container = sys.argv[1]
    tracemalloc.start()
    rows = read_rides_as('Data/ctabus.csv')
    print(f'Memory Use for container type RideData:  {tracemalloc.get_traced_memory()}')
    # find_largest_increase()
