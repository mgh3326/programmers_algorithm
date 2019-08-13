def solution(scoville: list, K):
    answer = -1
    scoville = sorted(scoville)
    result = 0
    while (True):
        if len(scoville) == 0:
            break
        if scoville[0] < scoville[1]:
            scoville[1] = scoville[0] + scoville[1] * 2
        else:
            scoville[1] = scoville[0] * 2 + scoville[1]
        result += 1
        if scoville[1] >= K and scoville[2] >= K:
            return result
        scoville.pop(0)
    return answer


scoville_list = [
    [1, 2, 3, 9, 10, 12]
]

k_list = [
    7

]
return_list = [
    2
]
for p, c, r in zip(scoville_list, k_list, return_list):
    print(scoville_list.index(p))
    result = solution(p, c)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
