import heapq


# TODO 제출 코드랑 비교하도록 하자

def solution(stock: int, dates: list, supplies: list, k: int):
    h = []
    answer = 0
    dates_index = 0
    len1 = len(dates)
    for i in range(k):
        stock -= 1
        if len1 > dates_index and i == dates[dates_index]:
            # dates.pop(0)
            supplies_pop = supplies[dates_index]
            dates_index += 1
            heapq.heappush(h, (supplies_pop * -1, supplies_pop))
        if stock == -1:
            heappop = heapq.heappop(h)[1]
            stock += heappop
            answer += 1
        if k - i < stock:
            break

    return answer


stock_list = [
    4
]
dates_list = [
    [4, 10, 15]

]
supplies_list = [
    [20, 5, 10]

]
k_list = [
    30

]
return_list = [
    2
]
for _0, _1, _2, _3, _4 in zip(stock_list, dates_list, supplies_list, k_list, return_list):
    print(stock_list.index(_0))
    result = solution(_0, _1, _2, _3)
    print(result)
    print(_4)
    if result == _4:
        print("맞음")
    else:
        print("틀림")
