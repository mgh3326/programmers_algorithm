import math


def solution(progresses: list, speeds: list):
    answer = []
    temp_list = []
    for progress, speeds in zip(progresses, speeds):
        temp = math.ceil((100 - progress) / speeds)
        temp_list.append(temp)
    index = 0
    temp_count = 0
    temp_max = 0
    for temp in temp_list:
        if temp_max == 0:
            temp_max = temp
            temp_count += 1
            continue
        else:
            if temp > temp_max:
                answer.append(temp_count)
                temp_count = 1
                temp_max = temp
            else:
                temp_count += 1
    answer.append(temp_count)
    return answer


progresses_list = [
    # [93, 30, 55],
    [40, 93, 30, 55, 60, 65],
    [93, 30, 55, 60, 40, 65]

]
speeds_list = [
    # [1, 30, 5],
    [60, 1, 30, 5, 10, 7],
    [1, 30, 5, 10, 60, 7]

]
return_list = [
    # [2, 1],
    [1, 2, 3],
    [2, 4]

]
for _p, _s, r in zip(progresses_list, speeds_list, return_list):
    print("index : ", end="")
    print(progresses_list.index(_p))
    result = solution(_p, _s)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
