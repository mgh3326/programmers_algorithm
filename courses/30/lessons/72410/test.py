import main


def test_solution1():
    result = main.solution("...!@BaT#*..y.abcdefghijklm")
    assert result == "bat.y.abcdefghi"


def test_solution2():
    result = main.solution("z-+.^.")
    assert result == "z--"


def test_solution3():
    result = main.solution("=.=")
    assert result == "aaa"


def test_solution4():
    result = main.solution("123_.def")
    assert result == "123_.def"


def test_solution5():
    result = main.solution("abcdefghijklmn.p")
    assert result == "abcdefghijklmn"
