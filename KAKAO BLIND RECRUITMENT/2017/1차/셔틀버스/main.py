import heapq


def solution(n, t, m, timetable: list):
    first_n = 9 * 60
    bus_time_list = [first_n]
    for i in range(n - 1):
        bus_time_list.append(first_n + t * (i + 1))

    sorted_minute_list = []
    minute_answer = bus_time_list[-1]
    for time in timetable:
        hour, minute = map(int, time.split(":"))
        minute += hour * 60
        heapq.heappush(sorted_minute_list, minute)
    is_end = False
    # 우선 순위 큐를 이용해보려고 하는데
    # 파이썬 우선 순위 큐의 경우 top이 없어서
    # pop을 하고 다시 top을 하는 행동이 오버헤드가 클까 라는 생각이 든다
    for bus_time in bus_time_list:
        if is_end == True:
            break
        current_m = 0
        while True:
            if current_m == m:
                break
            if len(sorted_minute_list) == 0:  # 자리가 남는다는걸 의미하네
                is_end = True
                break

            heappop = heapq.heappop(sorted_minute_list)
            if heappop <= bus_time:
                current_m += 1
            else:
                heapq.heappush(sorted_minute_list, heappop)
                break  # 다음 버스 보러가야되
    if current_m == m:
        minute_answer = heappop - 1
    if minute_answer // 60 < 10 and minute_answer % 60 < 10:
        answer = "0%d:0%d" % (minute_answer // 60, minute_answer % 60)
    elif minute_answer // 60 < 10:
        answer = "0%d:%d" % (minute_answer // 60, minute_answer % 60)
    elif minute_answer % 60 < 10:
        answer = "%d:0%d" % (minute_answer // 60, minute_answer % 60)
    else:
        answer = "%d:%d" % (minute_answer // 60, minute_answer % 60)

    return answer


n_list = [
    # 1,
    2, 2, 1, 1, 10
]
t_list = [
    # 1,
    10, 1, 1, 1, 60
]
m_list = [
    # 5,
    2, 2, 5, 1, 45
]
timetable_list = [
    # ["08:00", "08:01", "08:02", "08:03"],
    ["09:10", "09:09", "08:00"],
    ["09:00", "09:00", "09:00", "09:00"],
    ["00:01", "00:01", "00:01", "00:01", "00:01"],
    ["23:59"],
    ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
     "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"],

]
return_list = [
    # "09:00",
    "09:09",
    "08:59",
    "00:00",
    "09:00",
    "18:00",

]
for _input_data in zip(n_list, t_list, m_list, timetable_list, return_list):
    _0, _1, _2, _3 = _input_data[:-1]
    _r = _input_data[-1]
    print(n_list.index(_0))
    result = solution(_0, _1, _2, _3)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
