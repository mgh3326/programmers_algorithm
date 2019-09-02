import heapq


# TODO 제출 코드랑 비교하도록 하자
# day를 1씩 늘려갔는데, day의 값이 무척 커질때 20,000 까지 커지게 되면 오래 걸리게 된다. 이를 보완해주기 위해 stock의 값을 보고 day를 후다다닥 늘려주는 것이 필요하였다.

def solution(stock: int, dates: list, supplies: list, k: int):
    h = []
    answer = 0
    i = 0
    stock -= 1
    dates_index = 0
    len1 = len(dates)
    while True:
        if len1 > dates_index and i >= dates[dates_index]:
            while True:
                if len1 == dates_index or i < dates[dates_index]:
                    break
                supplies_pop = supplies[dates_index]
                dates_index += 1
                heapq.heappush(h, (supplies_pop * -1, supplies_pop))
        if stock == -1:
            heappop = heapq.heappop(h)[1]
            stock += heappop
            answer += 1
        if k - i < stock or i == k - 1:  # k-i 저거는 더 안봐도 되서 그런거
            break
        if i + (stock + 1) > k - 1:
            break
        else:
            i += (stock + 1)
            stock = -1
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
