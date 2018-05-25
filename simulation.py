#!/usr/bin/env python3


import argparse
from random import random
import sys


class ProbabilityDistributionError(Exception):
    """
    Exception used for distributions with probabilities not adding up to 1.
    """

def read_distribution(filename):
    """
    Read the file with the given name and return a probability distribution.

    The probability distribution is returned in a dictionary. It is expected
    that the given probabilities add up to 1.
    """
    distribution = {}
    with open(filename, encoding='utf-8') as f:
        f.readline()  # skip the header line
        for line in f:
            if len(line):
                demand, prob = line.split()
                demand, prob = int(demand), float(prob)
                distribution[demand] = prob
    if sum(distribution.values()) != 1:
        raise ProbabilityDistributionError
    return distribution


def simulate_total_demand(distribution, days):
    raise NotImplementedError


def main():
    """
    Run the given simulation from the command-line.
    """
    parser = argparse.ArgumentParser(
        description="Simulate future demand for bikes.")
    parser.add_argument("--filename", help="the input filename",
                        default="distribution.txt")
    parser.add_argument("--days", help="the number of days to simulate",
                        default=10, type=int)
    args = parser.parse_args()
    distribution = read_distribution(args.filename)
    total_demand = simulate_total_demand(distribution, args.days)
    print("The total demand for the next {} days is simulated to be {} bikes."
          .format(args.days, total_demand))


if __name__ == "__main__":
    sys.exit(main())
