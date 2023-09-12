import main


def test_solution1():
    result = main.solution(4)
    assert result == [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]


def test_solution2():
    result = main.solution(5)
    assert result == [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]


def test_solution3():
    result = main.solution(6)
    assert result == [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]
