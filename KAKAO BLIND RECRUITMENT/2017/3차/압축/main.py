def solution(msg):
    answer = []
    my_dict = {}
    dict_index = 1
    for i in ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
              "V", "W", "X", "Y", "Z"]:
        my_dict[i] = dict_index
        dict_index += 1
    temp_idx = 2
    for idx, my_msg in enumerate(msg):
        if temp_idx > 2:
            temp_idx -= 1
            continue

        temp_idx = 1
        while True:
            if idx + temp_idx > len(msg):
                answer.append(out_idx)
                break

            find_msg = msg[idx:idx + temp_idx]
            if find_msg in my_dict:
                temp_idx += 1
                out_idx = my_dict[find_msg]
                continue
            else:
                answer.append(out_idx)
                my_dict[find_msg] = dict_index
                dict_index += 1
                break

    return answer


msg_list = [
    "K",
    "KAKAO",
    "TOBEORNOTTOBEORTOBEORNOT",
    "ABABABABABABABAB"
]

return_list = [
    [11],
    [11, 1, 27, 15],
    [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34],
    [1, 2, 27, 29, 28, 31, 30]
]
for _input_data in zip(msg_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(msg_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
