import main


def test_solution1():
    result = main.solution(5, [[0, 0], [0, -1], [2, -3], [3, -3]])
    assert result == [33.0, 31.5, 0.0, -1.0]


def test_solution2():
    result = main.solution(3, [[0, 0], [1, -2], [3, -3]])
    assert result == [47.0, 36.0, 12.0]
