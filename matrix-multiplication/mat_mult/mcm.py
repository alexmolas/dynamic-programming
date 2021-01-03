from typing import Tuple

from mat_mult.base import MatrixChainMultiplication
from mat_mult.utils import memoize


class MCMNaive(MatrixChainMultiplication):
    def get_best_order(self, dims: Tuple[int]) -> str:
        ...

    def get_min_cost(self, dims: Tuple[int]) -> int:

        def _get_min_cost(dims_, i, j):
            """
            :param dims_: an array with the matrices dimensions
            :param i: initial index
            :param j: final index
            i and j define the subsequence of dims_ from which do we want to know the best ordering
            :return:
            """
            # base case, when we only have one matrix
            if j <= i + 1:
                return 0

            min_cost = float('inf')

            for k in range(i + 1, j):
                cost = _get_min_cost(dims_, i, k) + _get_min_cost(dims_, k, j) + dims_[i] * dims_[k] * dims_[j]
                if cost < min_cost:
                    min_cost = cost
            return min_cost
        return _get_min_cost(dims, 0, len(dims) - 1)


class MCMMemoization(MatrixChainMultiplication):
    def get_best_order(self, dims: Tuple[int]) -> str:
        ...

    def get_min_cost(self, dims: Tuple[int]) -> int:
        @memoize
        def _get_min_cost(dims_, i, j):
            """
            :param dims_: an array with the matrices dimensions
            :param i: initial index
            :param j: final index
            i and j define the subsequence of dims_ from which do we want to know the best ordering
            :return:
            """
            # base case, when we only have one matrix
            if j <= i + 1:
                return 0

            min_cost = float('inf')

            for k in range(i + 1, j):
                cost = _get_min_cost(dims_, i, k) + \
                       _get_min_cost(dims_, k, j) \
                       + dims_[i] * dims_[k] * dims_[j]
                if cost < min_cost:
                    min_cost = cost
            return min_cost

        return _get_min_cost(dims, 0, len(dims) - 1)
