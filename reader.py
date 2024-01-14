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

def read_csv_as_instances(filename, cls):
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        _ = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records
