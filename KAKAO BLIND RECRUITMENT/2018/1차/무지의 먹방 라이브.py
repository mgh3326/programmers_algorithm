import heapq


def solution(food_times: list, k):
    if k >= sum(food_times):
        return -1
    current_index = 0
    count = 0
    my_dict = {}
    my_list = []
    my_set = set()
    count_dict = {}
    for idx in range(len(food_times)):
        my_dict[idx] = idx + 1
        if food_times[idx] not in count_dict:
            count_dict[food_times[idx]] = 0
        count_dict[food_times[idx]] += 1
        if food_times[idx] not in my_set:
            heapq.heappush(my_list, food_times[idx])
            my_set.add(food_times[idx])
    min_sum = 0
    last_min = 0
    current_length = len(food_times)
    while True:
        if len(my_list) == 0:
            break
        heappop = heapq.heappop(my_list)
        min1 = heappop - min_sum
        min_sum += min1
        if k >= current_length * min1 + count:
            last_min = heappop
            count += current_length * min1
            current_length -= count_dict[heappop]
            # remove_list = []
            # for idx, food_time in enumerate(food_times):
            #     if min1 == food_time:
            #         remove_list.append(idx)
            #     else:
            #         food_times[idx] -= min1
            # for remove in reversed(remove_list):
            #     for i in range(len(food_times))[remove:-1]:
            #         my_dict[i] = my_dict[i + 1]
            #     my_dict.pop(len(food_times) - 1)
            #     food_times.pop(remove)
        else:
            break
    two_my_dict = {}
    two_index = 0
    two_food_times = []
    for my_dict_key in my_dict.keys():
        if food_times[my_dict_key] > last_min:
            two_my_dict[two_index] = my_dict[my_dict_key]
            two_index += 1
            two_food_times.append(food_times[my_dict_key] - last_min)

    count_ = (k - count) % current_length
    answer = two_my_dict[count_]
    return answer
    my_dict = two_my_dict
    food_times = two_food_times
    while True:

        if count == k:
            break

        food_times[current_index] -= 1
        if food_times[current_index] == 0:
            for i in range(len(food_times))[current_index:-1]:
                my_dict[i] = my_dict[i + 1]
            my_dict.pop(len(food_times) - 1)
            food_times.pop(current_index)
            current_index -= 1

        current_index += 1
        if current_index == len(food_times):
            current_index = 0
        count += 1
    answer = my_dict[current_index]
    return answer


food_times_list = [
    [3, 1, 2],
    [3, 1, 2],
    [3, 1, 2],
    [3, 1, 2, 2, 8],
]
k_list = [
    5, 6, 4,

    12
]

return_list = [
    1, -1, 3, 3
]
for _input_data in zip(food_times_list, k_list, return_list):
    _0, _1 = _input_data[:-1]
    _r = _input_data[-1]
    print(food_times_list.index(_0))
    result = solution(_0, _1)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
