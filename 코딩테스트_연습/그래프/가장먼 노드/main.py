def solution(n, edge):
    answer = 0

    edge_dict = {}
    status_list = [-1] * n
    for start, end in edge:
        start = start - 1
        end = end - 1
        if start not in edge_dict:
            edge_dict[start] = []
        if end not in edge_dict:
            edge_dict[end] = []
        edge_dict[start].append(end)
        edge_dict[end].append(start)
    status_list[0] = 0
    # BFS
    temp_list = [[0, edge_dict[0]]]
    while True:
        if len(temp_list) == 0:
            break
        start, end_list = temp_list.pop(0)
        for end in end_list:
            if status_list[end] == -1:
                status_list[end] = status_list[start] + 1
                pop_ = edge_dict[end]
                temp_list.append([end, pop_])
    answer = status_list.count(max(status_list))
    return answer


print(
    solution(
        6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    )
)
