import main


def test_solution1():
    result = main.solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]])
    assert result == 3


def test_solution2():
    result = main.solution(4, [[1, 2], [2, 3], [3, 4]])
    assert result == 0


def test_solution3():
    result = main.solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]])
    assert result == 1
