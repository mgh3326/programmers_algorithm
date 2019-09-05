def solution(lines):
    answer = 1
    on_time_list = make_on_time_list(lines)
    answer = find_answer(answer, on_time_list)

    return answer


def find_answer(answer, on_time_list):
    for idx, on_time in enumerate(on_time_list[:-1]):
        start_second, end_second = on_time
        temp_answer = 1
        for next_on_time in on_time_list[idx + 1:]:
            next_start_second, next_end_second = next_on_time
            if end_second + 1000 > next_start_second:
                temp_answer += 1
        if temp_answer > answer:
            answer = temp_answer
    return answer


def make_on_time_list(lines):
    on_time_list = []
    for line in lines:
        day, time, on_time = line.split()
        on_time = float(on_time[:-1])
        hour, minute, second = time.split(":")
        minute = int(hour) * 60 + int(minute)
        second = float(second)
        second += minute * 60
        start_second = int((second - on_time) * 1000) + 1
        end_second = int(second * 1000)
        on_time_list.append([start_second, end_second])
    return on_time_list


print(
    solution(
        ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
    )
)
