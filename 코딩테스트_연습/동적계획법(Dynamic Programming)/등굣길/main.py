dh = [1, 0, -1, 0]  # 하, 우, 상, 좌
dw = [0, 1, 0, -1]  # 하, 우, 상, 좌


def solution(m, n, puddles):
    def find_my_list_value(point_h, point_w):
        current_value = my_list[point_h][point_w]
        if current_value != -1:
            return current_value

        up_point = find_my_list_value(point_h - 1, point_w)  # 위
        left_point = find_my_list_value(point_h, point_w - 1)  # 좌
        my_list[point_h][point_w] = up_point + left_point
        return my_list[point_h][point_w]

    answer = 0
    # DFS로 접근하면서
    my_list = []
    for h in range(n):
        temp_list = []
        for w in range(m):
            temp_list.append(-1)
        my_list.append(temp_list)
    for puddle_h, puddle_w in puddles:
        my_list[puddle_w - 1][puddle_h - 1] = 0
    my_list[0][0] = 0
    is_puddle = False
    for h in range(n)[1:]:
        if is_puddle == True:
            my_list[h][0] = 0
        else:
            if my_list[h][0] == 0:
                is_puddle = True
            else:
                my_list[h][0] = 1
    is_puddle = False
    for w in range(m)[1:]:
        if is_puddle == True:
            my_list[0][w] = 0
        else:
            if my_list[0][w] == 0:
                is_puddle = True
            else:
                my_list[0][w] = 1
    answer = find_my_list_value(n - 1, m - 1)
    return answer % 1000000007


print(
    solution(
        4, 3, [[2, 2]]
    )
)

# 4
