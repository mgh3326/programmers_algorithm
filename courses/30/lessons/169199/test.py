import main


def test_solution1():
    result = main.solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])
    assert result == 7


def test_solution2():
    result = main.solution([".D.R", "....", ".G..", "...D"])
    assert result == -1
