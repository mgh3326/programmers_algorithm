import main


def test_solution1():
    result = main.solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
                           ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice",
                            "pot", "banana", "apple", "banana"])
    assert result == 3


def test_solution2():
    result = main.solution(["apple"], [10],
                           ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana",
                            "banana"])
    assert result == 0
