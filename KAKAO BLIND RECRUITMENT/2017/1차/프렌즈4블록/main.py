# TODO 레퍼런스 코드를 참고하여 함수로 깔끔하게 정리하는것도 필요할것으로 보인다.
def solution(m, n, board: list):
    # init
    answer = 0

    my_board_list = []
    for one_board in board:
        temp_list = []
        for str_one_board in one_board:
            temp_list.append(ord(str_one_board) - ord('A') + 1)
        my_board_list.append(temp_list)

    # 수행하기
    while True:
        remove_set = set()
        for i in range(m)[:-1]:
            for j in range(n)[:-1]:
                if my_board_list[i][j] == -1:
                    continue
                if (i > 0 and j > 0) and (
                        my_board_list[i][j] == my_board_list[i - 1][j - 1] == my_board_list[i - 1][j] ==
                        my_board_list[i][
                            j - 1]):  # 좌상
                    for _temp in [(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)]:
                        remove_set.add(_temp)
                if (j > 0) and (my_board_list[i][j] == my_board_list[i + 1][j - 1] == my_board_list[i + 1][j] ==
                                my_board_list[i][
                                    j - 1]):  # 좌하
                    for _temp in [(i, j), (i + 1, j - 1), (i + 1, j), (i, j - 1)]:
                        remove_set.add(_temp)
                if (i > 0) and (my_board_list[i][j] == my_board_list[i - 1][j + 1] == my_board_list[i - 1][j] ==
                                my_board_list[i][
                                    j + 1]):  # 우상
                    for _temp in [(i, j), (i - 1, j + 1), (i - 1, j), (i, j + 1)]:
                        remove_set.add(_temp)
                if my_board_list[i][j] == my_board_list[i + 1][j + 1] == my_board_list[i + 1][j] == my_board_list[i][
                    j + 1]:  # 우하
                    for _temp in [(i, j), (i + 1, j + 1), (i + 1, j), (i, j + 1)]:
                        remove_set.add(_temp)
        if len(remove_set) == 0:
            break
        for remove_set_value in remove_set:
            my_board_list[remove_set_value[0]][remove_set_value[1]] = -1
            answer += 1
        # 밑으로 내리기
        for i in range(n):
            is_end = False
            for j in reversed(range(m)):
                if is_end == True:
                    break
                if my_board_list[j][i] == -1:
                    for h in reversed(range(m)):
                        if h >= j:
                            continue
                        if my_board_list[h][i] != -1:
                            my_board_list[j][i] = my_board_list[h][i]
                            my_board_list[h][i] = -1
                            break
                        elif h == 0:
                            is_end = True

    return answer


m_list = [
    4, 6, 2, 2, 3,
    5
]
n_list = [
    5, 6, 2, 2, 2,
    3
]
board_list = [
    ["CCBDE", "AAADE", "AAABF", "CCBBF"],
    ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"],
    ["AA", "AA"],
    ["AA", "AC"],
    ["AA", "AA", "AC"],
    ["BCB", "CCC", "AAC", "AAC", "CAC"]

]
return_list = [
    14, 15, 4, 0, 6, 8
]
for _input_data in zip(m_list, n_list, board_list, return_list):
    _0, _1, _2 = _input_data[:-1]
    _r = _input_data[-1]
    print(m_list.index(_0))
    result = solution(_0, _1, _2)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
