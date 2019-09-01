def solution(weight):
    weight.sort()
    if weight[0] != 1:
        return 1
    sum_weight_list = []
    my_sum = 0
    answer = 0
    for i in range(len(weight[:-1])):
        my_sum += weight[i]
        sum_weight_list.append(my_sum)
        if my_sum + 1 < weight[i + 1]:
            answer = my_sum + 1
            return answer
    answer = sum_weight_list[-1] + weight[-1] + 1
    return answer


print(
    solution([3, 1, 6, 2, 7, 20, 1])
)
