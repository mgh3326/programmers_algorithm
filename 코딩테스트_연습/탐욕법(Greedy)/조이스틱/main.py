def solution(name: str):
    if name.count("A") == len(name):
        return 0
    alphabet_list = []
    my_list = []
    index_list = []
    for idx, i in enumerate(range(65, 91)):
        s = chr(i)
        alphabet_list.append(s)
    answer = 0
    for name_value in name:
        index = alphabet_list.index(name_value)
        answer += min(index, len(alphabet_list) - index)
    if 'A' in name:
        for idx, i in enumerate(name):
            if i == 'A':
                my_list.append(True)  # 끝
            else:
                if idx == 0:
                    pass
                else:
                    my_list.append(False)  # 가야되는거
                    index_list.append(idx)
        if len(index_list) != 0:
            if len(index_list) == 1:
                answer1 = index_list[0]
                answer2 = len(name) - index_list[0]

            else:
                answer1 = index_list[-1]
                answer2 = len(name) - index_list[0]
            answer += min(answer1, answer2)
    else:
        answer += len(name) - 1

    return answer


board_list = [
    # "JAN",
    "BAAA",
    "ABABAAAAAAABA"

]
return_list = [
    # 23,
    1, 4

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
