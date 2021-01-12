def memoize(f):
    memo = {}

    def helper(dims, i, j):
        if (i, j) not in memo:
            memo[(i, j)] = f(dims, i, j)
        return memo[(i, j)]
    return helper
