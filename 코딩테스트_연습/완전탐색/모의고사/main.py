def solution(answers):
    my_list = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    idx_list = [
        0, 0, 0
    ]
    count_list = [
        0, 0, 0
    ]
    result = []

    for answer_idx, answer in enumerate(answers):
        for my_idx, my in enumerate(my_list):
            if idx_list[my_idx] == len(my):
                idx_list[my_idx] = 0
            if my[idx_list[my_idx]] == answer:
                count_list[my_idx] += 1
            idx_list[my_idx] += 1
    max_count = max(count_list)
    for idx, count in enumerate(count_list):
        if count == max_count:
            result.append(idx + 1)

    return result


print(
    solution(
        [1, 2, 3, 4, 5]
    )
)
print(
    solution(
        [1, 3, 2, 4, 2]
    )
)
