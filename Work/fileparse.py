# fileparse.py
#
# Exercise 3.3

import csv

def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    csv 파일을 파싱해 레코드의 목록을 생성
    '''

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        if select and not has_headers:
            raise RuntimeError('select requires column headers') 

        # 헤더를 읽음
        headers = next(rows) if has_headers else []

        # 컬럼 선택기가 주어지면 지저한 컬럼의 인덱스를 찾는다.
        # 또한 결과 딕셔너리에 사용할 헤더의 집합을 좁힌다.
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for i, row in enumerate(rows, start=1):
            if not row:
                continue

            if indices:
                row = [ row[index] for index in indices ]

            # 딕셔너리를 만듦
            if types:
                try:
                    row = [ func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f"Row {i}: Couldn't convert {row}")
                        print(f"Row {i}: {e}")
                    continue

            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)

            records.append(record)

        return records
