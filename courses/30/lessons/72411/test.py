import main


# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]	[2,3,4]	["WX", "XY"]
def test_solution1():
    result = main.solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4], )
    assert result == ["AC", "ACDE", "BCFG", "CDE"]


def test_solution2():
    result = main.solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5])
    assert result == ["ACD", "AD", "ADE", "CD", "XYZ"]


def test_solution3():
    result = main.solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
    assert result == ["WX", "XY"]
