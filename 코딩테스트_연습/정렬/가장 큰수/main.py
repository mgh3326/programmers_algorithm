from functools import cmp_to_key


def solution(numbers):
    @cmp_to_key
    def my_cmp(p1, p2):
        if int(p1 + p2) > int(p2 + p1):
            return 1
        else:
            return -1

    if numbers.count(0) == len(numbers):
        return "0"
    str_numbers = []
    for number in numbers:
        str_numbers.append(str(number))
    # l = sorted(str_numbers, key=my_cmp, reverse=True)
    str_numbers.sort(key=my_cmp, reverse=True)
    answer = ''
    for _l in str_numbers:
        answer += _l

    return answer


print(
    solution(
        [6, 10, 2]
    )
)
# 6210
print(
    solution(
        [3, 30, 34, 5, 9]
    )
)
# 9534330
print(
    solution(
        [0, 0]
    )
)
