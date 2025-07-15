import main


def test_solution1():
    result = main.solution(3, [10, 100, 20, 150, 1, 100, 200])
    assert result == [10, 10, 10, 20, 20, 100, 100]


def test_solution2():
    result = main.solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])
    assert result == [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]
