import main


def test_solution1():
    result = main.solution([1, 1, 3, 3, 0, 1, 1])
    assert result == [1, 3, 0, 1]


def test_solution2():
    result = main.solution([4, 4, 4, 3, 3])
    assert result == [4, 3]
