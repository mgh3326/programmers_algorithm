import main


def test_solution1():
    result = main.solution([[2, 2, 6], [1, 5, 10], [4, 2, 9], [3, 8, 3]], 2, 2, 3)
    assert result == 4
