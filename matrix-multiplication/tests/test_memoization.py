from mat_mult.mcm import MCMMemoization


def test_naive_small(test_cases_small):
    for test in test_cases_small:
        dims = test['dims']
        solver = MCMMemoization()
        best_cost = solver.get_min_cost(dims=dims)
        assert best_cost == test['cost']


def test_naive_big(test_cases_big):
    for test in test_cases_big:
        dims = test['dims']
        solver = MCMMemoization()
        best_cost = solver.get_min_cost(dims=dims)
        assert best_cost == test['cost']
