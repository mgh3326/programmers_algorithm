import main

lottos_list = [[44, 1, 0, 0, 31, 25],
               [0, 0, 0, 0, 0, 0],
               [45, 4, 35, 20, 3, 9]
               ]
win_nums_list = [[31, 10, 45, 1, 6, 19],
                 [38, 19, 20, 40, 15, 25],
                 [20, 9, 3, 45, 4, 35]
                 ]
return_list = [[3, 5], [1, 6], [1, 1]]


def test_solution1():
    result = main.solution(lottos_list[0], win_nums_list[0])
    assert result == return_list[0]


def test_solution2():
    result = main.solution(lottos_list[1], win_nums_list[1])
    assert result == return_list[1]


def test_solution3():
    result = main.solution(lottos_list[2], win_nums_list[2])
    assert result == return_list[2]
