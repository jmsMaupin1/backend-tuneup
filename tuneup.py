#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "???"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper(file):
        profile = cProfile.Profile()
        profile.enable()
        results = func(file)
        profile.disable()
        stats = pstats.Stats(profile).sort_stats('cumulative')
        print('Results from: %s' % func.__name__)
        stats.print_stats()
        return results
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


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


@profile
def find_duplicate_movies_with_in(src):
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if movie in movies:
            duplicates.append(movie)
    return duplicates


@profile
def find_duplicate_movies_for_loop(src):
    movies = read_movies(src)
    duplicates = []
    for idx, movie in enumerate(movies):
        if movie in movies[idx + 1:]:
            duplicates.append(movie)

    return duplicates


@profile
def find_duplicate_movies_hash(src):
    movies = read_movies(src)
    duplicates = []
    movie_hash = {}

    for movie in movies:
        if movie not in movie_hash:
            movie_hash[movie] = 1
        else:
            duplicates.append(movie)

    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(lambda: find_duplicate_movies('movies.txt'))
    results = t.repeat(repeat=7, number=3)
    avg_time = min([time / 3 for time in results])
    print('Best time across 7 repeats of function 3 times is: %s' % avg_time)


def main():
    """Computes a list of duplicate movie entries"""
    # result = find_duplicate_movies('movies.txt')
    # with_in_results = find_duplicate_movies_with_in('movies.txt')
    # for_loop_results = find_duplicate_movies_for_loop('movies.txt')
    hash_results = find_duplicate_movies_hash('movies.txt')
    print('Found {} duplicate movies:'.format(len(hash_results)))
    print('\n'.join(hash_results))


if __name__ == '__main__':
    main()
