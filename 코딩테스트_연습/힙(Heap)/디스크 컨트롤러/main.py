import heapq


def solution(jobs):
    answer = 0
    time_list = []
    my_list = []
    time_dict = {}
    current_time = 0
    for job in jobs:
        in_time, timing = job  # 들어오는 시간, 진행 시간
        heapq.heappush(my_list, job)
    while True:
        if len(time_list) == 0 and len(my_list) == 0:
            break
        while True:
            if len(my_list) == 0:
                break
            job = heapq.heappop(my_list)
            if job[0] <= current_time:
                heapq.heappush(time_list, (job[1], job[0]))
            else:
                heapq.heappush(my_list, job)
                break
        if len(time_list) != 0:
            time_pop = heapq.heappop(time_list)
            answer += time_pop[0] + current_time - time_pop[1]
            current_time += time_pop[0]
        else:
            current_time += 1

    return answer // len(jobs)


print(

    solution(
        [[0, 3], [1, 9], [2, 6]]
    )
)
# 9
