#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)

mnames = ['user_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)


def test_users():
    print(users[:5])


def test_rating():
    print(ratings[:5])


def test_movies():
    print(movies[:5])


def test_merge_data():
    data = pd.merge(pd.merge(ratings, users), movies)
    # print(data.ix[0])
    mean_rating = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
    # print(mean_rating[:5])
    ratings_by_title = data.groupby('title').size()
    # print(ratings_by_title[:10])
    active_titles = ratings_by_title.index[ratings_by_title >= 250]
    # print(active_titles[:10])

    rating_std_by_title = data.groupby('title')['rating'].std()
    rating_std_by_title = rating_std_by_title.ix[active_titles]

    print(rating_std_by_title.order(ascending=False)[:10])

if __name__ == '__main__':
    test_merge_data()
