import math


def solution(progresses: list, speeds: list):
    answer = []
    temp_list = []
    for progress, speeds in zip(progresses, speeds):
        temp = math.ceil((100 - progress) / speeds)
        temp_list.append(temp)
    index = 0
    while True:

        max = temp_list[index]
        count = 0
        for temp in temp_list[index + 1:]:
            count += 1

            index += 1
            if temp > max:
                answer.append(count)
                break
        if index == len(temp_list) - 1:
            answer.append(count - 1)
            break

    return answer


progresses_list = [
    [93, 30, 55],
    [93, 93, 55],
    [30, 93, 55],

]
speeds_list = [
    [1, 30, 5],
    [1, 1, 5],
    [30, 1, 5],

]
return_list = [
    [2, 1],
    [2, 1],
    [1, 1, 1],

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
