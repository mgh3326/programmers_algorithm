import main


# k	tangerine	result
# 6	[1, 3, 2, 5, 4, 5, 2, 3]	3
# 4	[1, 3, 2, 5, 4, 5, 2, 3]	2
# 2	[1, 1, 1, 1, 2, 2, 2, 3]	1
def test_solution1():
    result = main.solution(6, [1, 3, 2, 5, 4, 5, 2, 3])
    assert result == 3


def test_solution2():
    result = main.solution(4, [1, 3, 2, 5, 4, 5, 2, 3])
    assert result == 2


def test_solution3():
    result = main.solution(2, [1, 1, 1, 1, 2, 2, 2, 3])
    assert result == 1
