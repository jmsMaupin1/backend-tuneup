#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import functools
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper():
        print('running %s' % func.__name__)
        func()
        print('done running %s' % func.__name__)

    return wrapper


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    for movie in movies:
        if movie.lower() == title.lower():
            return True
    return False


def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(lambda: find_duplicate_movies('movies.txt'))
    results = t.repeat(repeat=7, number=3)
    avg_time = min([time / 3 for time in results])
    print('Best time across 7 repeat of function calls 3 times is: %s' % avg_time)


@profile
def main():
    """Computes a list of duplicate movie entries"""
    timeit_helper()
    # result = find_duplicate_movies('movies.txt')
    # print('Found {} duplicate movies:'.format(len(result)))
    # print('\n'.join(result))


if __name__ == '__main__':
    main()
