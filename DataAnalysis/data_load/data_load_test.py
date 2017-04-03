#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pandas as pd
from pandas import Series


def test_read_csv():
    df = pd.read_csv('ex1.csv')
    # print(df)

    df = pd.read_table('ex1.csv', sep=',')
    # print(df)

    df = pd.read_csv('ex2.csv', header=None)
    print(df)


def test_read_big_data():
    result = pd.read_csv('ex6.csv', nrows=5)
    # print(result)
    chunker = pd.read_csv('ex6.csv', chunksize=1000)
    tot = Series([])
    for piece in chunker:
        tot = tot.add(piece['key'].value_counts(), fill_value=0)
    tot = tot.sort_values(ascending=False)
    print(tot)


def test_parse_xml():
    from lxml.html import parse
    from urllib2 import urlopen
    import requests

    parsed = parse(urlopen('http://finance.yahoo.com/q/op?s=AAPL+Options'))

    doc = parsed.getroot()

    print(doc)


def test_sqlite3():
    import sqlite3

    query = """
    CREATE TABLE test
    (a VARCHAR(20), b VARCHAR(20),
    c REAL,         d INTEGER
    );"""

    con = sqlite3.connect(':memory')
    con.execute(query)
    con.commit()

    data = [('Atlanta', 'Georgia', 1.25, 6),
            ('Tallahassee', 'Florida', 2.6, 3),
            ('Sacramento', 'California', 1.7, 5)]
    stmt = "INSERT INTO test VALUES(?, ?, ?, ?)"

    con.executemany(stmt, data)
    con.commit()


def test_read_from_sqlite3():
    import sqlite3
    con = sqlite3.connect(':memory')
    cursor = con.execute('select * from test')
    rows = cursor.fetchall()

    print(rows)

    import pandas.io.sql as sql
    print(sql.read_sql_query('select * from test', con))



if __name__ == '__main__':
    test_read_from_sqlite3()
