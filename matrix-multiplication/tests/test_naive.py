import csv
import os

import pytest

from mat_mult.mcm import MCMNaive

import sys
for p in sys.path:
    print(p)

THIS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def test_cases():
    tests = []
    path = os.path.join(THIS_DIR, 'test_cases.csv')
    with open(path) as file:
        test_cases = csv.reader(file)
        for row in test_cases:
            dims = [int(d) for d in row[0].split(' ')]
            cost = int(row[1])
            order = row[2]
            tests.append({'dims': dims, 'cost': cost, 'order': order})
    return tests


def test_naive(test_cases):
    for test in test_cases:
        dims = test['dims']
        solver = MCMNaive()
        best_cost = solver.get_min_cost(dims=dims)
        assert best_cost == test['cost']
