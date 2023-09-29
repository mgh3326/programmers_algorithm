import main


def test_solution1():
    result = main.solution("100-200*300-500+20")
    assert result == 60420


def test_solution2():
    result = main.solution("50*6-3*2")
    assert result == 300
