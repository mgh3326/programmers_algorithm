def solution(s):
    split = list(map(int, s.split()))

    return str(min(split)) + " " + str(max(split))


board_list = [
    "1 2 3 4",
    "-1 -2 -3 -4",
    "-1 -1",

]
return_list = [
    "1 4",
    "-4 -1",
    "-1 -1",

]
for _input_data in zip(board_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(board_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
