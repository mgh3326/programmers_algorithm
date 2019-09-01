def solution(board: list):
    board_dict = {}
    find_dict = {}
    answer = 0
    # 보드 정보 딕셔너리에 저장
    for h, board_width_list in enumerate(board):
        for w, board_value in enumerate(board_width_list):
            if board_value != 0:
                if board_value not in board_dict:
                    board_dict[board_value] = []
                board_dict[board_value].append((h, w))
    # 저장된 보드 정보 딕셔너리를 확인하여, 채워야할 딕셔너리를 생성
    for board_dict_key in board_dict.keys():
        key_ = board_dict[board_dict_key]
        h_min = min(key_, key=lambda x: x[0])[0]
        h_max = max(key_, key=lambda x: x[0])[0]
        w_min = min(key_, key=lambda x: x[1])[1]
        w_max = max(key_, key=lambda x: x[1])[1]
        for h in range(h_min, h_max + 1):
            for w in range(w_min, w_max + 1):
                if (h, w) not in key_:
                    if (h, w) not in find_dict:
                        find_dict[(h, w)] = []
                    find_dict[(h, w)].append(board_dict_key)
    # 맨 위부터 2칸씩 채워보도록 하자!
    is_end = False
    while True:
        if is_end == True:
            break
        is_end = True

        found_dict = {}
        for w in range(len(board[0])):
            for h in range(len(board)):
                if board[h][w] != 0:
                    if h - 1 >= 0:
                        if (h - 1, w) in find_dict:
                            dict_value_list = find_dict[(h - 1, w)]
                            for dict_value in dict_value_list:
                                if dict_value not in found_dict:
                                    found_dict[dict_value] = []
                                found_dict[dict_value].append((h - 1, w))
                    if h - 2 >= 0:
                        if (h - 2, w) in find_dict:
                            dict_value_list = find_dict[(h - 2, w)]
                            for dict_value in dict_value_list:
                                if dict_value not in found_dict:
                                    found_dict[dict_value] = []
                                found_dict[dict_value].append((h - 2, w))
                    break
        for found_dict_key in found_dict.keys():
            if len(found_dict[found_dict_key]) == 2:
                answer += 1
                is_end = False
                for value in board_dict[found_dict_key]:
                    board[value[0]][value[1]] = 0
                board_dict.pop(found_dict_key)
                for remove_value in found_dict[found_dict_key]:
                    if len(find_dict[remove_value]) == 1:
                        find_dict.pop(remove_value)
                    else:
                        find_dict[remove_value].remove(found_dict_key)

    return answer


board_list = [
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 4, 0, 0, 0], [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
     [0, 0, 0, 0, 3, 0, 4, 0, 0, 0], [0, 0, 0, 2, 3, 0, 0, 0, 5, 5], [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
     [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

]
return_list = [
    2
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
