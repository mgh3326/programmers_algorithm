import main


def test_solution1():
    result = main.solution([[40, 10000], [25, 10000]], [7000, 9000])
    assert result == [1, 5400]


def test_solution2():
    result = main.solution([[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]],
                           [1300, 1500, 1600, 4900])
    assert result == [4, 13860]
