from mat_mult.mcm import memoized_mcm


def test_memo(test_cases):
    for test in test_cases:
        dims = test['dims']
        best_cost = memoized_mcm(dims=dims)[0]
        assert best_cost == test['cost']
