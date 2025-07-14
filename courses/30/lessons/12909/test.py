import main


# s	answer
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false
def test_solution1():
    result = main.solution("()()")
    assert result == True


def test_solution2():
    result = main.solution("(())()")
    assert result == True


def test_solution3():
    result = main.solution(")()(")
    assert result == False


def test_solution4():
    result = main.solution("(()(")
    assert result == False
