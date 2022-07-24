def solution(numbers, hand):
    left_point = [0, 3]
    right_point = [2, 3]

    number_hash = {
        1: [0, 0],
        2: [1, 0],
        3: [2, 0],
        4: [0, 1],
        5: [1, 1],
        6: [2, 1],
        7: [0, 2],
        8: [1, 2],
        9: [2, 2],
        0: [1, 3],
    }
    answer = ''
    for number in numbers:
        target_point = number_hash[number]
        if target_point[0] == 0:
            answer += "L"
            left_point = target_point
        elif target_point[0] == 2:
            answer += "R"
            right_point = target_point
        else:
            left_value = abs(left_point[0] - target_point[0]) + abs(left_point[1] - target_point[1])
            right_value = abs(right_point[0] - target_point[0]) + abs(right_point[1] - target_point[1])
            if left_value < right_value:
                answer += "L"
                left_point = target_point
            elif left_value > right_value:
                answer += "R"
                right_point = target_point
            else:  # equal
                if hand == "left":
                    answer += "L"
                    left_point = target_point
                else:
                    answer += "R"
                    right_point = target_point
    return answer
