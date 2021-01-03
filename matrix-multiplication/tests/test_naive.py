from mat_mult.mcm import MCMNaive


def test_naive(test_cases_small):
    for test in test_cases_small:
        dims = test['dims']
        solver = MCMNaive()
        best_cost = solver.get_min_cost(dims=dims)
        assert best_cost == test['cost']
