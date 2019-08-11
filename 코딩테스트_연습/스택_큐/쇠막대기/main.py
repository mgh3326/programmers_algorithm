def solution(arrangement):
    stack = []
    lazer_list = []
    poll_list = {}
    answer = 0

    # yes enum
    # for idx, value in enumerate(arrangement):
    # no enum
    for _i in range(len(arrangement)):
        idx = _i
        value = arrangement[_i]
        if value == "(":
            stack.append(idx)
        else:
            pop = stack.pop()
            if pop + 1 == idx:
                answer += len(stack)
                # # 레이저
                # lazer_list.append(idx)
            else:
                answer += 1
                # for i in range(pop, idx):
                #     if i in poll_list:
                #         poll_list[i] += 1
                #     else:
                #         poll_list[i] = 1

    # for lazer in lazer_list:
    #     if lazer in poll_list:
    #         answer += poll_list[lazer]
    return answer


arrangement_list = [
    "()(((()())(())()))(())",

]
return_list = [
    17,

]
for _h, r in zip(arrangement_list, return_list):
    print("index : ", end="")
    print(arrangement_list.index(_h))
    result = solution(_h)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
