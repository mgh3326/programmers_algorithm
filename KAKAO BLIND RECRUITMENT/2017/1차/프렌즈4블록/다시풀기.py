def solution(m, n, board):
    answer = 0
    for idx, board_value in enumerate(board):
        board[idx] = list(board_value)
    while True:
        game = block_game(board, m, n)
        if game == -1:
            break
        else:
            answer += game

    return answer


def block_game(board, m, n):
    remove_set = set()
    for h in range(m)[:-1]:
        for w in range(n)[:-1]:
            left_up = board[h][w]
            left_down = board[h + 1][w]
            right_up = board[h][w + 1]
            right_down = board[h + 1][w + 1]
            if left_up == 0 or left_down == 0 or right_up == 0 or right_down == 0:
                continue
            if left_up == left_down == right_up == right_down:
                remove_set.add((h, w))
                remove_set.add((h + 1, w))
                remove_set.add((h, w + 1))
                remove_set.add((h + 1, w + 1))
    if len(remove_set) == 0:
        return -1

    change_w_set = remove_block(board, remove_set)
    rebuild(board, change_w_set, m)
    return len(remove_set)


def rebuild(board, change_w_set, m):
    for w in change_w_set:
        is_end = False
        for _h in range(m):
            if is_end:
                break
            h = m - _h - 1
            if board[h][w] == 0:
                for _find_non_zero_h_index in range(_h + 1, m):
                    find_non_zero_h_index = m - _find_non_zero_h_index - 1
                    if board[find_non_zero_h_index][w] != 0:
                        board[h][w] = board[find_non_zero_h_index][w]
                        board[find_non_zero_h_index][w] = 0
                        break
                    if find_non_zero_h_index == 0:  # 0까지 모두 0임을 의미한다. (백트레킹)
                        is_end = True


def remove_block(board, remove_set):
    change_w_set = set()
    for h, w in remove_set:
        change_w_set.add(w)
        board[h][w] = 0
    return change_w_set


print(
    solution(
        4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]
    )
)
# 14
