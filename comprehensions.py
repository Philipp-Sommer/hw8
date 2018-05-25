#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to learn how to use list comprehensions.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Clemens Eichberger <clemens.eichberger@edu.uni-graz.at>
"""

from factor import is_prime
import numpy as np


def divisors(number):
    """
    Returns all divisors of a given number.

    >>> divisors(10)
    [1, 2, 5]
    """
    lis = [x for x in range(1, number) if number % x == 0]
    return lis


def filter_by_first_letter(strings, letter):
    """
    Filters strings by first letter.

    >>> filter_by_first_letter(['a', 'b', 'aa', 'bb'], 'a')
    ['a', 'aa']
    """
    key = letter.lower()
    lis = [x for x in strings if x[0].lower() == key]
    return lis


def primes(number):
    """
    Returns all primes up to a given number.

    >>> primes(3)
    [1, 2, 3]
    """
    end = number + 1
    lis = [x for x in range(end) if is_prime(x)]
    return lis


def roll_n_times(n):
    """
    Rolls a dice n-times and records results.

    >>> np.random.seed(1)
    >>> roll_n_times(5)
    [4, 5, 1, 2, 4]
    """
    lis = list(np.random.randint(1, 6, n))
    return lis

if __name__ == "__main__":
    import doctest
    doctest.testmod()