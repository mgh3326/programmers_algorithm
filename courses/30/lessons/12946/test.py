import main


def test_solution1():
    result = main.solution(1)
    assert result == [[1, 3]]


def test_solution2():
    result = main.solution(2)
    assert result == [[1, 2], [1, 3], [2, 3]]
