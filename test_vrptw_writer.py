#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for vrtpw writer

.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Clemens Eichberger <clemens.eichberger@edu.uni-graz.at>
"""
import pandas as pd
import vrptw_writer
import unittest


class TestVrptwWriter(unittest.TestCase):

    def test_by_demand(self):
        msg = 'By demand failed!'
        inp = 'by_id.txt'
        out = 'f_demand.csv'
        check_df = pd.read_csv('by_demand.txt', sep='\s+').astype(int)
        vrptw_writer.write_file(inp, out, 'DEMAND')
        self.assertTrue(pd.read_csv(out).equals(check_df), msg)

    def test_by_due_date(self):
        msg = 'By due date failed!'
        inp = 'by_id.txt'
        out = 'f_due.csv'
        check_df = pd.read_csv('by_due.txt', sep='\s+').astype(int)
        vrptw_writer.write_file(inp, out, 'DUE_DATE')
        self.assertTrue(pd.read_csv(out).equals(check_df), msg)

    def test_by_rdy(self):
        msg = 'By ready time failed!'
        inp = 'by_id.txt'
        out = 'f_rdy.csv'
        check_df = pd.read_csv('by_rdy.txt', sep='\s+').astype(int)
        vrptw_writer.write_file(inp, out, 'READY_TIME')
        self.assertTrue(pd.read_csv(out).equals(check_df), msg)


if __name__ == "__main__":
    unittest.main()
