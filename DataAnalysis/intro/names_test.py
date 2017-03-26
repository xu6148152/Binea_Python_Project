#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pandas as pd

years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces, ignore_index=True)

# print(names)

total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)

print(total_births.tail())

total_births.plot(title='Total births by sex and year').get_figure().savefig("output3.png")