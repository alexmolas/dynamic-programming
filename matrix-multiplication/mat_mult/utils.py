import random
from typing import Sequence

from mat_mult.mcm import memoized_mcm


def generate_test_cases(n_tests: int, min_len: int, max_len: int, min_dim: int, max_dim: int) \
        -> Sequence[Sequence[int]]:
    """

    :param n_tests: number of test to generate
    :param min_len: minimum number of matrices for each test case
    :param max_len: maximum number of matrices for each test case
    :param min_dim: minimum dimension for each matrix (applies both for rows and columns)
    :param max_dim: maximum dimension for each matrix (applies both for rows and columns)
    :return:
    """
    solutions = []
    for n in range(n_tests):
        test_len = random.randint(min_len, max_len)
        dims = tuple([random.randint(min_dim, max_dim) for _ in range(test_len)])
        solution = memoized_mcm(dims=dims)[0]
        solutions.append([dims, solution])
    return solutions


def print_parenthesis(i, j, s):
    if i == j:
        name = chr(65 + i)
        print(name, end="")
        return
    else:
        print("(", end="")
        print_parenthesis(i, s[i][j] - 1, s)
        print_parenthesis(s[i][j], j, s)
        print(")", end="")
