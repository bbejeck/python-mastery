# reader.py

import csv
import logging
log = logging.getLogger(__name__)


def convert_csv(lines, converter, *, headers=None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    for row in rows:
        try:
            records.append(converter(headers, row))
        except ValueError as e:
            log.warning(f'Bad row {row}')
            log.debug(f'Reason : {e}')

    return records


def csv_as_dicts(lines, types, *, headers=None):
    return convert_csv(lines,
                lambda headers, row: {name: func(val) for name, func, val in zip(headers, types, row)})


def csv_as_instances(lines, cls, *, headers=None):
    return convert_csv(lines,
                lambda headers, row: cls.from_row(row))


def read_csv_as_instances(filename, cls):
    with open(filename) as file:
        return csv_as_instances(file, cls)


def read_csv_as_dicts(filename, types):
    with open(filename) as file:
        return csv_as_dicts(file, types)
