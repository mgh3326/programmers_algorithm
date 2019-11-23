def solution(n, build_frame):
    answer = []
    board_list = [[list() for _ in range(n + 1)] for _ in range(n + 1)]
    for x, y, a, b in build_frame:
        y = n - y
        if a == 0:  # 기둥
            if b == 1:  # 설치
                if y == n or (0 in board_list[y + 1][x]) or 1 in board_list[y][x] or 1 in board_list[y][x - 1]:  # 끝
                    board_list[y][x].append(0)
            else:  # 삭제
                is_ok = True
                if 0 in board_list[y - 1][x]:  # 위에 기둥이 있을  때
                    # 아래 보가 있으면 되겠다
                    if 1 in board_list[y - 1][x] or 1 in board_list[y - 1][x - 1]:
                        pass
                    else:
                        is_ok = False
                if 1 in board_list[y - 1][x]:  # 위에 보가 있을  때
                    # 왼쪽 아래 기둥 있을때 혹은 양쪽이 보 연결
                    if (1 in board_list[y - 1][x - 1] and 1 in board_list[y - 1][x + 1]) or 0 in board_list[y][x + 1]:
                        pass
                    else:
                        is_ok = False
                if 1 in board_list[y - 1][x - 1]:  # 왼쪽 위에 보가 있을  때
                    # 오른쪽 아래 기둥 있을때 혹은 양쪽 보 연결
                    if (1 in board_list[y - 1][x - 2] and 1 in board_list[y - 1][x]) or 0 in board_list[y][x - 1]:
                        pass
                    else:
                        is_ok = False
                if is_ok:
                    board_list[y][x].remove(0)
        else:  # 보
            if b == 1:  # 설치
                if 0 in board_list[y + 1][x] or 0 in board_list[y + 1][x + 1] or (
                        1 in board_list[y][x - 1] and 1 in board_list[y][x + 1]):  # 끝
                    board_list[y][x].append(1)
            else:  # 삭제
                is_ok = True
                if 0 in board_list[y][x]:  # 본 위치에 기둥이 있을  때
                    # 왼쪽에 보가 있으면 되겠다
                    if 1 in board_list[y][x - 1]:
                        pass
                    else:
                        is_ok = False
                if 0 in board_list[y][x + 1]:  # 오른쪽에 기둥이 있을  때
                    # 오른쪽에 보가 있으면 되겠다
                    if 1 in board_list[y][x + 1]:
                        pass
                    else:
                        is_ok = False
                if 1 in board_list[y][x - 1]:  # 왼쪽 보가 있을  때
                    # (기둥이 있으면 되겠다.) 왼쪽 보 아래 본래 보 아래
                    if 0 in board_list[y][x] or 0 in board_list[y][x - 1]:
                        pass
                    else:
                        is_ok = False
                if 1 in board_list[y][x + 1]:  # 오른쪽 보가 있을  때
                    # (기둥이 있으면 되겠다.) 오른쪽 보, 오른쪽 오른쪽 보
                    if 0 in board_list[y][x + 2] or 0 in board_list[y][x + 1]:
                        pass
                    else:
                        is_ok = False
                if is_ok:
                    board_list[y][x].remove(1)
    for w in range(n + 1):
        for _h in range(n + 1):
            h = n - _h
            print(w,h)
            if len(board_list[h][w]) == 1:
                answer.append([w, _h, board_list[h][w][0]])
            elif len(board_list[h][w]) == 2:
                answer.append([w, _h, 0])
                answer.append([w, _h, 1])
    return answer


print(
    solution(
        5,
        [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
    )
)
