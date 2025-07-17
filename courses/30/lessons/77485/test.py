import main


def test_solution1():
    result = main.solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
    assert result == [8, 10, 25]


def test_solution2():
    result = main.solution(3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]])
    assert result == [1, 1, 5, 3]


def test_solution3():
    result = main.solution(100, 97, [[1, 1, 100, 97]])
    assert result == [1]
