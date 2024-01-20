from abc import ABC, abstractmethod


class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass


class TextTableFormatter(TableFormatter):
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-' * 10 + ' ') * len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(','.join(str(h) for h in headers))

    def row(self, rowdata):
        print(','.join(str(r) for r in rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print('<tr>', ''.join(f'<th>{h}</th>' for h in headers), '</tr>')

    def row(self, rowdata):
        print('<tr>', ''.join(f'<td>{h}</td>' for h in rowdata), '</tr>')


class ColumnFormatMixin:
    formats = []

    def row(self, rowdata):
        rowdata = [(fmt % d) for fmt, d in zip(self.formats, rowdata)]
        super().row(rowdata)


class UpperHeadersMixin:
    def headings(self, headers):
        super().headings([h.upper() for h in headers])


def create_formatter(format, column_formats=None, upper_headers=False):
    if format == 'csv':
        formatter_cls = CSVTableFormatter
    elif format == 'html':
        formatter_cls = HTMLTableFormatter
    elif format == 'text':
        formatter_cls = TextTableFormatter
    else:
        raise RuntimeError(f'Unrecognized formate {format}')

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
            formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()



def print_table(records, fields, formatter):
    if not isinstance(formatter, TableFormatter):
        raise TypeError('Expected a TableFormatter')

    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
