dh = [1, 0, -1, 0]  # 하 우 상 좌
dw = [0, 1, 0, -1]  # 하 우 상 좌
status_dict = {}

answer = -1


def solution(maps):
    global answer

    def dfs(point, depth):
        global answer
        if point == find_point:
            if answer == -1 or answer > depth:
                answer = depth
            return
        if answer != -1 and depth >= answer:  # 백 트래킹
            return
        possible_point_list = []
        for i in range(len(dh)):
            nh = dh[i]
            nw = dw[i]
            current_h, current_w = point
            next_point = current_h + nh, current_w + nw
            if next_point in status_dict:
                if status_dict[next_point]:
                    possible_point_list.append(next_point)
        if len(possible_point_list) > 1:
            possible_point_list.sort(key=lambda x: abs(find_point[0] - x[0]) + abs(
                find_point[1] - x[1]))

        for possible_point in possible_point_list:
            status_dict[possible_point] = False
            dfs(possible_point, depth + 1)
            status_dict[possible_point] = True

    answer = -1
    status_dict.clear()
    map_height = len(maps)
    map_width = len(maps[0])
    start_point = (0, 0)
    find_point = (map_height - 1, map_width - 1)
    for h in range(map_height):
        for w in range(map_width):
            if maps[h][w] == 1:
                status_dict[h, w] = True
    status_dict[start_point] = False
    dfs(start_point, 1)
    return answer


print(
    solution(
        [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
    )
)
# 11
print(
    solution(
        [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
    )
)
# -1
