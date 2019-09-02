def solution(baseball):
    all_list = []
    for i in range(1, 10):
        for j in range(1, 10):
            if i == j:
                continue
            for k in range(1, 10):
                if i == k or j == k:
                    continue
                all_list.append([str(i), str(j), str(k)])

    answer = 0
    for number, strike, ball in baseball:
        remove_list = []
        for all_value in all_list:
            temp_strike = 0
            temp_ball = 0
            for number_value in str(number):
                if number_value in all_value:
                    if str(number).index(number_value) == all_value.index(number_value):
                        temp_strike += 1
                    else:
                        temp_ball += 1
            if temp_strike == strike and temp_ball == ball:
                pass
            else:
                remove_list.append(all_value)
        for remove in remove_list:
            all_list.remove(remove)

    return len(all_list)


print(
    solution(
        [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
    )
)
