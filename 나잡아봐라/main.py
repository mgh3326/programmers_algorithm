# bfs를 이용하여, 모든 경우를 생각하여 풀었다. BFS를 사용하되, DP도 같이 사용하면 효율이 올라갈듯 하다.
def solution(c, b):  # 코니 위치, 브라운 위치
    brown_speed_list = [-1, 1, 0]
    result = -1
    position_min = 0
    position_max = 200000
    cony_position = c
    brown_position = b
    cony_speed = 1
    depth = 0
    queue = []
    queue.append([brown_position, cony_position, cony_speed, depth])
    while True:
        if cony_position > position_max or cony_position < position_min:
            break
        if len(queue) == 0:
            break
        brown_position, cony_position, cony_speed, depth = queue.pop(0)
        # bfs로 짜고 queue에 브라운 위치, 코니 위치, 코니 속도 이렇게 넣어주면 될 듯하다.
        for brown_speed in brown_speed_list:
            if brown_speed == 0:
                next_brown_position = brown_position * 2
            else:
                next_brown_position = brown_position + brown_speed
            if next_brown_position > position_max or next_brown_position < 0:
                continue
            next_cony_position = (cony_position + cony_speed)
            if next_brown_position == next_cony_position:
                result = depth + 1
                break
            queue.append([next_brown_position, next_cony_position, cony_speed + 1, depth + 1])
        if result > -1:
            break

    # 1, 2

    return result


print(
    solution(6, 3)
)
# 5
