import heapq


def solution(people, limit):
    answer = 0
    people.sort()
    asc_index = 0
    desc_index = len(people) - 1
    while True:
        if asc_index > desc_index:
            break
        if asc_index > desc_index:
            answer += 1
            break
        if people[asc_index] + people[desc_index] <= limit:
            asc_index += 1
            desc_index -= 1
            answer += 1
        else:
            desc_index -= 1
            answer += 1

    return answer


# print(
#     solution(
#         [40, 40, 40], 100
#     )
# )
# print(
#     solution(
#         [70, 50, 80, 50], 100
#     )
# )
print(
    solution(
        [70, 80, 50], 100
    )
)
