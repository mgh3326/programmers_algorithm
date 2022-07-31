import main

a_list = [[1, 2, 3, 4], [-1, 0, 1]]
b_list = [[-3, -1, 0, 2], [1, 0, -1]]
result_list = [3, -2]


def test_solution1():
    a = a_list[0]
    b = b_list[0]
    result = main.solution(a, b)
    assert result == result_list[0]


def test_solution2():
    a = a_list[1]
    b = b_list[1]
    result = main.solution(a, b)
    assert result == result_list[1]
