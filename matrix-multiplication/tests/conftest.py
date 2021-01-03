import pytest
import csv

import os
THIS_DIR = os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def test_cases_big():
    tests = []
    path = os.path.join(THIS_DIR, 'test_cases_big.csv')
    with open(path) as file:
        test_cases = csv.reader(file)
        for row in test_cases:
            dims = [int(d) for d in row[0].split(' ')]
            cost = int(row[1])
            order = row[2]
            tests.append({'dims': dims, 'cost': cost, 'order': order})
    return tests


@pytest.fixture
def test_cases_small():
    tests = []
    path = os.path.join(THIS_DIR, 'test_cases_small.csv')
    with open(path) as file:
        test_cases = csv.reader(file)
        for row in test_cases:
            dims = [int(d) for d in row[0].split(' ')]
            cost = int(row[1])
            order = row[2]
            tests.append({'dims': dims, 'cost': cost, 'order': order})
    return tests
