import main

s_list = ["one4seveneight",
          "23four5six7",
          "2three45sixseven",
          "123",
          "onetwo1zero"
          ]
return_list = [1478, 234567, 234567, 123, 1210]


def test_solution1():
    result = main.solution(s_list[0])
    assert result == return_list[0]


def test_solution2():
    result = main.solution(s_list[1])
    assert result == return_list[1]


def test_solution3():
    result = main.solution(s_list[2])
    assert result == return_list[2]


def test_solution4():
    result = main.solution(s_list[3])
    assert result == return_list[3]


def test_solution5():
    result = main.solution(s_list[4])
    assert result == return_list[4]
