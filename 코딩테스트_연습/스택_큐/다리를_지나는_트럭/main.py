def solution(bridge_length: int, weight: int, truck_weights: list):
    answer = 0
    current_weight = 0
    current_truck_list = []
    while True:
        if len(truck_weights) == 0 and len(current_truck_list) == 0:
            break
        answer += 1
        current_weight = 0
        for current_truck in current_truck_list:
            current_truck[1] -= 1
            current_weight += current_truck[0]

        for current_truck in current_truck_list:
            if current_truck[1] == 0:
                current_truck_list.remove(current_truck)
                current_weight -= current_truck[0]

        if len(truck_weights) != 0 and current_weight + truck_weights[0] <= weight:
            pop = truck_weights.pop(0)
            current_truck_list.append([pop, bridge_length])

    return answer


bridge_length_list = [
    2,
    100,
    100

]

weight_list = [
    10,
    100,
    100
]
truck_weights_list = [
    [7, 4, 5, 6],
    [10],
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
]
return_list = [
    8,
    101,
    110
]
for _1, _2, _3, r in zip(bridge_length_list, weight_list, truck_weights_list, return_list):
    print("index : ", end="")
    print(bridge_length_list.index(_1))
    result = solution(_1, _2, _3)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
