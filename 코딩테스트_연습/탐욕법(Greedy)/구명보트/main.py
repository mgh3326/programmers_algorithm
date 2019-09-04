import heapq


def solution(people, limit):
    answer = 0
    person_list = []
    person_desc__list = []

    for person in people:
        heapq.heappush(person_list, person)
        heapq.heappush(person_desc__list, person * -1)
    answer += len(person_list)
    if len(person_list) == 0 or len(person_list) == 1:
        return answer
    person_min = heapq.heappop(person_list)
    person_max = heapq.heappop(person_desc__list) * -1
    person_list.remove(person_max)
    person_desc__list.remove(person_min * -1)

    while True:

        if person_min + person_max <= limit:
            # 둘이 한칸 들어갔어 둘다 한번씩 빼줘야되
            answer -= 1
            if len(person_list) == 0 or len(person_list) == 1:
                return answer
            person_min = heapq.heappop(person_list)
            person_max = heapq.heappop(person_desc__list) * -1
            person_list.remove(person_max)
            person_desc__list.remove(person_min * -1)

        else:  # 못들어간다리 Max만 조신히 들어가도록 하자
            if len(person_list) == 0:
                return answer
            person_max = heapq.heappop(person_desc__list) * -1
            person_list.remove(person_max)

    return answer


# print(
#     solution(
#         [40, 40, 40], 100
#     )
# )
print(
    solution(
        [70, 50, 80, 50], 100
    )
)
# print(
#     solution(
#         [70, 80, 50], 100
#     )
# )
