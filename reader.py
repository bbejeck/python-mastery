import csv
import sys


def read_csv_as_dicts(file, coltypes):
    dict_list = []
    with open(file) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for header in headers:
            sys.intern(header)
        for row in rows:
            dict_list.append({name: func(val) for func, name, val in zip(coltypes, headers, row)})
    return dict_list
