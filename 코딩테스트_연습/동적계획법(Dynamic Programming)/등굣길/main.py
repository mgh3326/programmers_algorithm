dh = [1, 0, -1, 0]  # 하, 우, 상, 좌
dw = [0, 1, 0, -1]  # 하, 우, 상, 좌


def solution(m, n, puddles):
    answer = 0
    # DFS로 접근하면서
    my_list = []
    for h in range(n):
        temp_list = []
        for w in range(m):
            temp_list.append(-1)
        my_list.append(temp_list)
    for puddle_h, puddle_w in puddles:
        my_list[puddle_w - 1][puddle_h - 1] = -2
    my_list[0][0] = 0
    point_list = [[0, 0]]
    while True:
        if len(point_list) == 0:
            break
        current_h, current_w = point_list.pop(0)
        if current_h == n - 1 and current_w == m - 1:
            answer += 1
        current_value = my_list[current_h][current_w]
        for dir_idx in range(len(dh)):
            nh = current_h + dh[dir_idx]
            nw = current_w + dw[dir_idx]
            if nh < 0 or nw < 0 or nh >= n or nw >= m:
                continue
            next_value = my_list[nh][nw]
            if next_value == -2:
                continue
            if next_value == -1:
                my_list[nh][nw] = current_value + 1
            if next_value == -1 or next_value >= current_value + 1:
                point_list.append((nh, nw))
    return answer % 1000000007


print(
    solution(
        4, 3, [[2, 2]]
    )
)

# 4
