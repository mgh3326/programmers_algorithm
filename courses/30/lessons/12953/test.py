import main


def test_solution1():
    result = main.solution([2, 6, 8, 14])
    assert result == 168


def test_solution2():
    result = main.solution([1, 2, 3])
    assert result == 6
