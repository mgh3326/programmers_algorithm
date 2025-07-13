import main


def test_solution1():
    result = main.solution(["X591X", "X1X5X", "X231X", "1XXX1"])
    assert result == [1, 1, 27]


def test_solution2():
    result = main.solution(["XXX", "XXX", "XXX"])
    assert result == [-1]

def test_solution3():
    result = main.solution(["XXXXXXXXXXXXXX", "XXXXXXXXXXXXXX", "XXXXXXXXXXXXXX"])
    assert result == [-1]
