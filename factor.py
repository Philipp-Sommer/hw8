#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This program will factorize any given integer.

It should work for every integer, but be aware that very large numbers
might take long to factorize, depending on the number and size of the
needed prime factors.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
"""

import numpy as np


class NumberToFactor(object):
    """
    This class is used to factor a given integer and print the solution.
    If print_solution gets set to False nothing gets printed, but primality
    and factors still get calculated.
    """

    def __init__(self, inp, print_solution=True):
        self.number = inp
        self.prime = is_prime(self.number)
        self.text = '{} ='.format(self.number)
        if self.prime:
            print(self.text, '1 *', self.number)
        else:
            self.solution = factorize(self.number)
            if print_solution:
                self.print_solution(self.solution)

    def print_solution(self, arr):
        for x in arr:
            self.text += ' {} *'.format(int(x))
        print(self.text[:-2])


def factorize(number):
    """
    Returns an array of all prime factors of an integer.
    """
    array = np.empty(0, dtype=int)

    for x in [2, 3]:
        if number % x == 0:
            array = np.append(array, x)
            while number % (np.product(array) * x) == 0:
                array = np.append(array, x)

    if np.product(array) == number:
        return array

    elif is_prime(number / np.product(array)):
        array = np.append(array, number / np.product(array))
        return array

    else:
        count = 5
        tes = 0
        while not is_prime(number / np.product(array)):
            y = count + 2
            tes += 1
            if tes == 500:
                print(count)
                tes = 0
            if number % count == 0:
                while number % (np.product(array) * count) == 0:
                    array = np.append(array, count)
                    print('add', count)
            if number % y == 0:
                while number % (np.product(array) * y) == 0:
                    array = np.append(array, y)
                    print('add', y)
            count += 6
        if np.product(array) == number:
            return array
        else:
            array = np.append(array, number // np.product(array))
            return array


def is_prime(number):
    """
    Checks primality of an integer.
    """
    if number == 2 or number == 3 or number == 5:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    else:
        count = 5
        while count <= int(number**0.5):
            if number % count == 0 or number % (count + 2) == 0:
                return False
            else:
                count += 6
        return True


if __name__ == "__main__":
    inp = int(input('Integer: '))
    test = NumberToFactor(inp)
