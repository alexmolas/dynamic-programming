from typing import Tuple, Sequence

from mat_mult.decorators import memoize


def naive_mcm(dims: Tuple[int]) -> Tuple[int, Sequence]:
    n_matrices = len(dims) - 1
    s = [[0 for _ in range(n_matrices)] for _ in range(n_matrices)]

    def _mcm(d, i, j):
        if j <= i + 1:
            return 0

        min_cost = float('inf')

        best_partition = None

        for k in range(i + 1, j):
            cost = _mcm(d, i, k) + _mcm(d, k, j) + d[i] * d[k] * d[j]
            if cost < min_cost:
                min_cost = cost
                best_partition = k
        s[i][j - 1] = best_partition
        return min_cost
    return _mcm(dims, 0, n_matrices), s


def memoized_mcm(dims: Tuple[int]) -> Tuple[int, Sequence]:
    n_matrices = len(dims) - 1
    s = [[0 for _ in range(n_matrices)] for _ in range(n_matrices)]

    @memoize
    def _mcm(d, i, j):
        if j <= i + 1:
            return 0

        min_cost = float('inf')

        best_partition = None

        for k in range(i + 1, j):
            cost = _mcm(d, i, k) + _mcm(d, k, j) + d[i] * d[k] * d[j]
            if cost < min_cost:
                min_cost = cost
                best_partition = k
        s[i][j - 1] = best_partition
        return min_cost

    return _mcm(dims, 0, n_matrices), s
