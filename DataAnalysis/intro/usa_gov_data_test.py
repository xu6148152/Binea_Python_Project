#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import json

path = 'usagov_bitly_data2012-03-16-1331923249.txt'

records = [json.loads(line) for line in open(path, encoding='utf-8')]


def test_tz_data():
    print(records[0]['tz'])


def test_timezone():
    time_zones = [rec['tz'] for rec in records if 'tz' in rec]
    # print(time_zones)

    counts = get_counts(time_zones)
    print(counts['America/New_York'])

    # print(get_top_counts(counts, 10))
    from collections import Counter
    counts = Counter(time_zones)
    print(counts.most_common(10))


def get_counts(sequence):
    from collections import defaultdict

    counts = defaultdict(int)
    for x in sequence:
        counts[x] += 1
    return counts


def get_top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]


def test_pandas():
    from pandas import DataFrame, Series
    import pandas as pd;
    import numpy as np


    frame = DataFrame(records)

    # print(frame)
    # print(frame['tz'][:10])
    tz_counts = frame['tz'].value_counts()
    # print(tz_counts[:10])

    clean_tz = frame['tz'].fillna('Missing')
    clean_tz[clean_tz == ''] = 'Unknown'
    tz_counts = clean_tz.value_counts()

    import matplotlib.pyplot as plt

    tz_counts[:10].plot(kind='barh', rot=0).get_figure().savefig("output.png")

    results = Series([x.split()[0] for x in frame.a.dropna()])
    # print(results[:5])
    # print(results.value_counts()[:8])

    cframe = frame[frame.a.notnull()]
    operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
    # print(operating_system[:5])
    by_tz_os = cframe.groupby(['tz', operating_system])
    agg_counts = by_tz_os.size().unstack().fillna(0)
    # print(agg_counts[:10])

    indexer = agg_counts.sum(1).argsort()
    # print(indexer[:10])

    count_subset = agg_counts.take(indexer)[-10:]
    # print(count_subset)
    # count_subset.plot(kind='barh', stacked=True).get_figure().savefig("output2.png")

    normed_subset = count_subset.div(count_subset.sum(1), axis=0)
    normed_subset.plot(kind='barh', stacked=True).get_figure().savefig("output2.png")

if __name__ == '__main__':
    test_pandas()
