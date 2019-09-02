def solution(prices):
    answer = [0] * len(prices)
    my_dict = {}
    for idx, price in enumerate(prices):
        for value in (my_dict.values()):
            for my_value in value:
                answer[my_value] += 1

        l = list(filter(lambda x: x > price, my_dict.keys()))
        for i in l:
            my_dict.pop(i)
        if price not in my_dict:
            my_dict[price] = []
        my_dict[price].append(idx)

    return answer


print(
    solution(
        [1, 2, 3, 2, 3]
    )
)
