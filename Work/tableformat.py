# tableformat.py
#
# Exercise 4.5

class TableFormatter:
    def headings(self, headers):
        '''
        테이블 헤딩을 반환
        '''
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

        #raise NotImplementedError()


    def row(self, rowdata):
        '''
        테이블 데이터의 단일 행을 반환
        '''
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

        #raise NotImplementedError()
        

class CSVTableFormatter(TableFormatter):
    '''
    포트폴리오 데이터를 CSV 포맷으로 출력
    '''
    def headings(self, headers):
        print(','.join(headers))

    
    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
    '''
    포트폴리오 데이터를 HTML 형식으로 출력
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')

        
class TextTableFormatter(TableFormatter):
    '''
    포트폴리오 데이터를 텍스트 형식으로 출력
    '''
    def headings(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f'{d:>10s}', end=' ')
        print()

class FormatError(Exception):
    pass

def create_formatter(name):
    '''
    주어진 포맷에 맞는 포매터를 생성한다.
    '''
    if name == 'txt':
        return TextTableFormatter()
    elif name == 'csv':
        return CSVTableFormatter()
    elif name == 'html':
        return HTMLTableFormatter()
    else:
        raise FormatError(f'Unknown table format {name}')


def print_table(objects, columns, formatter):
    '''
    오브젝트와 어트리뷰트명으로 잘 모맷된 테이블을 만든다.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [ str(getattr(obj, name)) for name in columns ]
        formatter.row(rowdata)