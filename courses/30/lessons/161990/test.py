import main


def test_solution1():
    result = main.solution([".#...", "..#..", "...#."])
    assert result == [0, 1, 3, 4]


def test_solution2():
    result = main.solution(["..........", ".....#....", "......##..", "...##.....", "....#....."])
    assert result == [1, 3, 5, 8]


def test_solution3():
    result = main.solution([".##...##.", "#..#.#..#", "#...#...#", ".#.....#.", "..#...#..", "...#.#...", "....#...."])
    assert result == [0, 0, 7, 9]


def test_solution4():
    result = main.solution(["..", "#."])
    assert result == [1, 0, 2, 1]
