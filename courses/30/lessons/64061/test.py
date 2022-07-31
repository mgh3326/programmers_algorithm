import main


def test_solution1():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5, 1, 2, 1, 4])
    assert result == 4


def test_solution2():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5, 1, 2, 1, 4, 2, 5])
    assert result == 6


def test_solution3():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5, 1, 2, 1, 4, 5, 2])
    assert result == 6


def test_solution4():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5, 1, 2, 1, 4, 5, 1, 1, 1, 1, 2])
    assert result == 6


def test_solution5():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5])
    assert result == 2


def test_solution6():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5, 1])
    assert result == 4


def test_solution7():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
                           [1, 5, 3, 5, 1, 2, 2])
    assert result == 6


def test_solution10():
    result = main.solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                           [1, 5, 3, 5, 1, 2, 1, 4, 5, 1, 1, 1, 1, 2])
    assert result == 0
