#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module writes sorted vrtpw problems to new files.

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Clemens Eichberger <clemens.eichberger@edu.uni-graz.at>
"""
import pandas as pd


def write_file(input_file, write_to, sort_by):
    """
    Reads a vrptw file, sorts it by a given key and writes the solution
    to a csv file.

    >>> write_file('r101.txt', 'f_doc.csv', 'DEMAND')
    >>> pd.read_csv('f_doc.csv').equals(pd.read_csv('r101_by_demand.csv'))
    True
    """
    data = pd.read_csv(input_file, sep='\s+')
    data_sorted = data.sort_values([sort_by, 'CUST_NO.']).astype(int)
    out = data_sorted.set_index('CUST_NO.')
    out.to_csv(write_to)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
