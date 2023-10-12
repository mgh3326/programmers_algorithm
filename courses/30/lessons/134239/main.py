def calculate_hailstone_sequence(n, result):
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    result.append(n)
    if n > 1:
        calculate_hailstone_sequence(n, result)


def solution(k, ranges):
    answer = []
    sequence = [k]
    calculate_hailstone_sequence(k, sequence)
    y_value_list = sequence
    area_list = []
    n = len(y_value_list)
    for i in range(n - 1):
        area_list.append((y_value_list[i] + y_value_list[i + 1]) / 2)
    for s1, s2 in ranges:
        diff = n + s2
        if s1 >= diff:
            area_sum = -1
        elif s1 == diff - 1:
            area_sum = 0
        else:
            area_sum = sum(area_list[s1:diff - 1])
        answer.append(area_sum)
    return answer
