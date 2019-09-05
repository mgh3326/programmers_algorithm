def solution(dartResult):
    dartResult = dartResult.replace("10", "a")
    number_list = []
    for i in range(10):
        number_list.append(str(i))
    number_list.append("a")
    score_list = [0] * 3
    current_idx = -1
    for i in dartResult:
        if i in number_list:
            current_idx += 1
            if i == 'a':
                score_list[current_idx] = 10
            else:
                score_list[current_idx] = int(i)
        elif i == "S":
            score_list[current_idx] = pow(score_list[current_idx], 1)
        elif i == "D":
            score_list[current_idx] = pow(score_list[current_idx], 2)
        elif i == "T":
            score_list[current_idx] = pow(score_list[current_idx], 3)
        elif i == "#":
            score_list[current_idx] *= -1
        elif i == "*":
            score_list[current_idx] *= 2
            if current_idx != 0:
                score_list[current_idx - 1] *= 2
    answer = sum(score_list)
    return answer


print(
    solution(
        "1S*2T*3S"
    )
)
#
print(
    solution(
        "1D2S#10S"
    )
)
# 9
print(
    solution(
        "1D2S0T"
    )
)
# 3
