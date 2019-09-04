import heapq


def solution(people, limit):
    answer = 0
    person_list = []
    person_desc__list = []
    average = limit // 2
    is_to_add = False
    people_count = people.count(average)
    answer += people_count // 2
    if people_count % 2 == 1:
        is_to_add = True

    for person in people:
        if person == average:
            pass
        else:
            heapq.heappush(person_list, person)
            heapq.heappush(person_desc__list, person * -1)
    if is_to_add == True:  # 에버리지 값은 짝수 개를 지워야하므로 일단 다 지움
        heapq.heappush(person_list, average)
        heapq.heappush(person_desc__list, average * -1)
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
            if len(person_list) == 0 or len(person_list) == 1:
                return answer
            person_max = heapq.heappop(person_desc__list) * -1
            person_list.remove(person_max)

    return answer


print(
    solution(
        [40, 40, 40], 100
    )
)
# print(
#     solution(
#         [70, 50, 80, 50], 100
#     )
# )
# print(
#     solution(
#         [70, 80, 50], 100
#     )
# )
