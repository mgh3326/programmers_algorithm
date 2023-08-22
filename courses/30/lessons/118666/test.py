import main


def test_solution1():
    result = main.solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5])
    assert result == "TCMA"


def test_solution2():
    result = main.solution(["TR", "RT", "TR"], [7, 1, 3])
    assert result == "RCJA"
