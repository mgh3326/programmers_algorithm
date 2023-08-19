import main


def test_solution1():
    result = main.solution(["aya", "yee", "u", "maa", "wyeoo"])
    assert result == 1


def test_solution2():
    result = main.solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"])
    assert result == 3
