import heapq


def solution(n, t, m, timetable):
    answer = ''
    time_list = []
    for timetable_value in timetable:
        hour, minute = map(int, timetable_value.split(":"))
        minute += hour * 60
        heapq.heappush(time_list, minute)
    start_minute = 9 * 60
    for bus_start_time_index in range(n):
        current_minute = start_minute + bus_start_time_index * t
        temp_list = []
        for bus_count_index in range(m):
            if len(time_list) == 0:
                break
            heappop = heapq.heappop(time_list)
            if heappop > current_minute:
                heapq.heappush(time_list, heappop)

                break
            else:
                temp_list.append(heappop)
    if len(temp_list) < m:
        answer_minute = current_minute
    else:
        answer_minute = temp_list[-1] - 1
    answer_hour = str(answer_minute // 60)
    answer_minute = str(answer_minute % 60)
    if len(answer_hour) == 1:
        answer_hour = '0' + answer_hour
    if len(answer_minute) == 1:
        answer_minute = '0' + answer_minute
    answer = answer_hour + ":" + answer_minute
    return answer


print(
    solution(
        1, 1, 1, ["09:10"]
    )
)
print(
    solution(
        1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
    )
)

print(
    solution(
        2, 10, 2, ["09:10", "09:09", "08:00"]
    )
)
