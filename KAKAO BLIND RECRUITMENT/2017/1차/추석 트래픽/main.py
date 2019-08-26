def line_to_seconds(line):
    time, progressed_second = line.split(" ")[1:]
    hour, minute, second = map(float, time.split(":"))
    minute += hour * 60
    second += minute * 60
    second = int(second * 1000)
    start_second = second - int(float(progressed_second[:-1]) * 1000) + 1
    return start_second, second


def solution(lines: list):
    second_list = []
    answer = 1
    # 간격이 1초 이상만 벌어진다면 다음 리스트로 생각해도 무방할것 같다
    for line in lines:
        second_list.append(line_to_seconds(line))
    for second_idx in range(len(second_list)):
        second = second_list[second_idx]
        start_second, last_second = second
        count = 1
        for two_second_idx in range(len(second_list))[second_idx + 1:]:
            two_second = second_list[two_second_idx]
            two_start_second, two_last_second = two_second

            if (two_start_second <= last_second <= two_last_second) or (
                    two_start_second <= last_second + 999):
                count += 1
                if count > answer:
                    answer = count
            else:
                if last_second < two_last_second - 4000:  # 백트래킹을 3000으로 생각해서 틀렸다
                    break

    return answer


lines_list = [
    [
        # "2016-09-15 23:59:59.001 2.0s",
        "2016-09-15 01:00:04.001 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ],
    [
        "2016-09-15 01:00:04.002 2.0s",
        "2016-09-15 01:00:07.000 2s"
    ],
    [
        "2016-09-15 20:59:57.421 0.351s",
        "2016-09-15 20:59:58.233 1.181s",
        "2016-09-15 20:59:58.299 0.8s",
        "2016-09-15 20:59:58.688 1.041s",
        "2016-09-15 20:59:59.591 1.412s",
        "2016-09-15 21:00:00.464 1.466s",
        "2016-09-15 21:00:00.741 1.581s",
        "2016-09-15 21:00:00.748 2.31s",
        "2016-09-15 21:00:00.966 0.381s",
        "2016-09-15 21:00:02.066 2.62s"
    ]
]

return_list = [
    1,
    2,
    7
]
for _0, _1, in zip(lines_list, return_list):
    print(lines_list.index(_0))
    result = solution(_0)
    print(result)
    print(_1)
    if result == _1:
        print("맞음")
    else:
        print("틀림")
