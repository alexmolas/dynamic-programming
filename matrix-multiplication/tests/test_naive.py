from mat_mult.mcm import naive_mcm


def test_naive(test_cases):
    for test in test_cases:
        dims = test['dims']
        best_cost = naive_mcm(dims=dims)[0]
        assert best_cost == test['cost']
