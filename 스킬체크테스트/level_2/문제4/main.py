def solution(citations: list):
    answer = 1
    count = 0
    for citation in citations:
        if citation >= answer:
            count += 1
    if count >= answer and (len(citations) - count) <= answer:
        return answer
    answer += 1


n_list = [

    [3, 0, 6, 1, 5]
]

return_list = [

    3
]
for p, r in zip(n_list, return_list):
    print(n_list.index(p))
    result = solution(p)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
