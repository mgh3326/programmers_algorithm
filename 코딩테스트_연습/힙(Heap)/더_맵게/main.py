import heapq


def solution(scoville: list, K):
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    answer = 0

    while True:
        if len(h) == 0:
            answer = -1
            break
        else:
            s1 = heapq.heappop(h)

            if s1 >= K:
                break
            elif len(h) == 0:
                answer = -1
                break
        s2 = heapq.heappop(h)
        heapq.heappush(h, s1 + 2 * s2)
        answer += 1

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
