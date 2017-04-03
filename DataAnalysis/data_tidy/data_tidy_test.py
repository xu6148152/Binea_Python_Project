#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

from pandas import DataFrame
import pandas as pd


def test_merge():
    df1 = DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'], 'data1': range(7)})

    df2 = DataFrame({'key': ['a', 'b', 'd'], 'data2': range(3)})

    print(df1)
    print(df2)

    result = pd.merge(df1, df2, on='key')
    print(result)


def test_tidy_food_data():
    import json

    db = json.load(open('foods-2011-10-03.json'))
    # print(len(db))
    # print(db[0].keys())
    nutrients = DataFrame(db[0]['nutrients'])
    # print(nutrients[:7])

    info_keys = ['description', 'group', 'id', 'manufacturer']

    info = DataFrame(db, columns=info_keys)

    # print(info[:5])
    # print(pd.value_counts(info.group)[:10])

    nutrients = []
    for rec in db:
        fnuts = DataFrame(rec['nutrients'])
        fnuts['id'] = rec['id']
        nutrients.append(fnuts)

    nutrients = pd.concat(nutrients, ignore_index=True)
    # print(nutrients)

    # print(nutrients.duplicated().sum())
    nutrients = nutrients.drop_duplicates()

    col_mapping = {'description': 'food',
                   'group': 'fgroup'}
    info = info.rename(columns=col_mapping, copy=False)
    col_mapping = {'description': 'nutrient',
                   'group': 'nutgroup'}
    nutrients = nutrients.rename(columns=col_mapping, copy=False)

    ndata = pd.merge(nutrients, info, on='id', how='outer')
    # print(ndata)

    result = ndata.groupby(['nutrient', 'fgroup'])['value'].quantile(0.5)
    result['Zinc, Zn'].order().plot(kind='barh').get_figure().savefig("output.png")


if __name__ == '__main__':
    test_tidy_food_data()
