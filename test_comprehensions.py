#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testing suite for comprehension module.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Clemens Eichberger <clemens.eichberger@edu.uni-graz.at>
"""

import unittest
import comprehensions
import numpy as np


class TestComprehensions(unittest.TestCase):

    def test_divisors(self):
        failmsg = 'div failed'
        self.assertEqual(comprehensions.divisors(12), [1, 2, 3, 4, 6],
                         failmsg)

    def test_filter(self):
        failmsg = 'Filter failed!'
        list_ = ['aa', 'bb', 'cc', 'dd', 'be', 'abc', 'bbd']

        self.assertEqual(comprehensions.filter_by_first_letter(list_, 'a'),
                         ['aa', 'abc'], failmsg)
        self.assertEqual(comprehensions.filter_by_first_letter(list_, 'b'),
                         ['bb', 'be', 'bbd'], failmsg)

    def test_primes(self):
        failmsg = 'Primes failes!'

        self.assertEqual(comprehensions.primes(15),
                         [1, 2, 3, 5, 7, 11, 13], failmsg)

    def test_roll(self):
        failmsg = 'Roll failed!'
        np.random.seed(1)
        self.assertEqual(comprehensions.roll_n_times(5), [4, 5, 1, 2, 4],
                         failmsg)
        self.assertEqual(len(comprehensions.roll_n_times(5)), 5, failmsg)


if __name__ == "__main__":
    unittest.main()
