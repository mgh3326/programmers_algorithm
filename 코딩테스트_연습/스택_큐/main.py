def solution(priorities, location):
    answer = 0
    while True:
        if len(priorities) == 0:
            return answer + 1
        current_priority = priorities.pop(0)
        location -= 1
        if location == -2:
            location = len(priorities) - 1

        for idx, priority in enumerate(priorities):
            if current_priority < priority:
                priorities.append(current_priority)
                break
            if idx == len(priorities) - 1:
                answer += 1
                if location == -1:
                    return answer


priorities_list = [
    # [2, 1, 3, 2],
    # [1, 1, 9, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
location_list = [
    # 2,
    # 0,
    5

]
return_list = [
    # 1,
    # 5,
    1

]
for p, c, r in zip(priorities_list, location_list, return_list):
    print(priorities_list.index(p))
    result = solution(p, c)
    print(result)
    if result == r:
        print("맞음")
    else:
        print("틀림")
