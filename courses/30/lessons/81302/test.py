import main


def test_solution1():
    result = main.solution(
        [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
         ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
         ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
    assert result == [1, 0, 1, 1, 1]
