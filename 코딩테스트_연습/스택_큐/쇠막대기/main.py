def solution(arrangement):
    stack = []
    answer = 0
    for idx in range(len(arrangement)):
        value = arrangement[idx]
        if value == "(":
            stack.append(idx)
        else:
            pop = stack.pop()
            if pop + 1 == idx:
                answer += len(stack)
            else:
                answer += 1
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
