import main


# ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["young", "john", "tod", "emily", "mary"]	[12, 4, 2, 5, 10]	[360, 958, 108, 0, 450, 18, 180, 1080]
# ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]	["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]	["sam", "emily", "jaimie", "edward"]	[2, 3, 5, 4]	[0, 110, 378, 180, 270, 450, 0, 0]

def test_solution1():
    result = main.solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                           ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                           ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10])
    assert result == [360, 958, 108, 0, 450, 18, 180, 1080]


def test_solution2():
    result = main.solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                           ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                           ["sam", "emily", "jaimie", "edward"], [2, 3, 5, 4])
    assert result == [0, 110, 378, 180, 270, 450, 0, 0]
