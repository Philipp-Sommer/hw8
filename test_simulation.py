#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for simulation


.. moduleauthor:: Philipp Sommer <philipp.sommer@edu.uni-graz.at>
.. moduleauthor:: Clemens Eichberger <clemens.eichberger@edu.uni-graz.at>
"""

import unittest
import simulation


class TestSimulation(unittest.TestCase):
    """
    Test class for simulation
    """
    def test_two(self):
        """
        sjldfnkjadnkjdvanödjnva
        asöfjnafjnföajn
        >>>
        """
        msg = 'not close to expected value'
        dis = {1: 0.5, 3: 0.5}

        result = simulation.simulate_total_demand(dis, 10**6)
        self.assertAlmostEqual(result / 10**6, 2, delta=0.005, msg=msg)

    def test_easy(self):
        """
        aödnfondvnadipnvdaöj
        aöfifbnlana

        >>>
        """
        msg = 'there was a false outcome'
        dis = {100: 1, 3: 0}

        result = simulation.simulate_total_demand(dis, 10)
        self.assertAlmostEqual(result / 10, 100, msg=msg)


if __name__ == "__main__":
    unittest.main()
