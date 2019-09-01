import heapq


def solution(N, stages):  # 스테이지 개수,
    my_list = []
    temp_list = []
    my_dict = {}
    for stage in stages:
        heapq.heappush(my_list, stage)
    current_index = 1
    while True:
        total_len = len(my_list)
        count = 0
        if current_index == N + 1:
            break
        if len(my_list) > 0:
            heappop = heapq.heappop(my_list)
            count += 1
            while True:

                if heappop == current_index:
                    if len(my_list) == 0:
                        break

                    heappop = heapq.heappop(my_list)
                    count += 1
                else:
                    heapq.heappush(my_list, heappop)
                    count -= 1
                    break
        if total_len == 0:
            if 0 not in my_dict:
                my_dict[0] = []
            my_dict[0].append(current_index)
            temp_list.append(0)
        else:
            if count / total_len not in my_dict:
                my_dict[count / total_len] = []
            my_dict[count / total_len].append(current_index)
            temp_list.append(count / total_len)

        current_index += 1
    answer = []
    for my_dict_key in sorted(my_dict.keys(), reverse=True):
        for my_dict_value in my_dict[my_dict_key]:
            answer.append(my_dict_value)

    return answer


N_list = [
    5, 4, 2
]
stages_list = [
    [2, 1, 2, 6, 2, 4, 3, 3],
    [4, 4, 4, 4, 4],
    [1, 1, 2, 2, 2],
]

return_list = [
    [3, 4, 2, 1, 5],
    [4, 1, 2, 3],
    [4, 1, 2, 3, 5]
]
for _input_data in zip(N_list, stages_list, return_list):
    _0, _1 = _input_data[:-1]
    _r = _input_data[-1]
    print(N_list.index(_0))
    result = solution(_0, _1)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
