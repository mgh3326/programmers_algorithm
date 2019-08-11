def solution(heights):
    answer = []
    answer.append(0)
    for idx, height in enumerate(heights[1:]):
        for i in range(idx + 1):
            _height = heights[idx - i]
            if _height > height:
                answer.append(idx - i + 1)
                break
            if i == idx:
                answer.append(0)

    return answer


heights_list = [
    [6, 9, 5, 7, 4],
    [3, 9, 9, 3, 5, 7, 2],
    [1, 5, 3, 6, 7, 6, 5]
]
return_list = [
    [0, 0, 2, 2, 4],
    [0, 0, 0, 3, 3, 3, 6],
    [0, 0, 2, 0, 0, 5, 6]

]
for _h, r in zip(heights_list, return_list):
    print("index : ", end="")
    print(heights_list.index(_h))
    result = solution(_h)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
