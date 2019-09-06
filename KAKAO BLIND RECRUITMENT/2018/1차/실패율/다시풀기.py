import heapq


def solution(N, stages):
    answer = []
    stages.sort()
    result_list = []
    current_stage_count = 1
    current_stage_index = 0
    saved_index = 0
    temp_count = 0
    while True:
        if len(stages) == 0 or current_stage_count > N:
            for i in range(current_stage_count, N + 1):
                result_list.append((0, i))
            break
        count = 0
        length = len(stages)
        while True:
            if len(stages) == 0:
                break
            stage = stages[0]
            if stage > current_stage_count:
                break
            else:
                count += 1
                stages.pop(0)
        result_list.append((-1 * count / length, current_stage_count))
        current_stage_count += 1
    result_list.sort(key=lambda x: (x[0], x[1]))
    while True:
        if len(result_list) == 0:
            break
        heappop = result_list.pop(0)
        answer.append(heappop[1])
    return answer


print(
    solution(
        1, [2, 2, 2, 6, 2, 4, 3, 3]
    )
)
