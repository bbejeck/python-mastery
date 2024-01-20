class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()


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


def create_formatter(format):
    if format == 'csv':
        return CSVTableFormatter()
    elif format == 'html':
        return HTMLTableFormatter()
    else:
        return TextTableFormatter()


def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
