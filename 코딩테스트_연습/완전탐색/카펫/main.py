import math


def solution(brown, red):
    answer = []
    total_sum = brown + red
    temp_list = []
    for i in range(3, int(math.sqrt(total_sum)) + 1):
        if total_sum % i == 0:
            temp_list.append([total_sum // i, i])
    for temp in temp_list:
        height, width = temp
        width_ = 2 * (height + width) - 4
        if width_ == brown:
            return temp
    return answer


print(
    solution(
        10, 2
    )
)
print(
    solution(
        8, 1
    )
)
print(
    solution(
        24, 24
    )
)
