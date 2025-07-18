import re

import main


def test_solution1():
    result = main.solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
    assert result == 2


def test_solution2():
    result = main.solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
    assert result == 2


def test_solution3():
    result = main.solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
    assert result == 3
