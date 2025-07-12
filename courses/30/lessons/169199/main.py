def solution(board):
    d_values_set = set()
    for h in range(len(board)):
        for w in range(len(board[h])):
            if board[h][w] == "R":
                r_values = (h, w)
            elif board[h][w] == "G":
                g_values = (h, w)
            elif board[h][w] == "D":
                d_values_set.add(tuple([h, w]))
    h_len = len(board)
    w_len = len(board[0])
    # BFS 접근이라고 생각이 든다
    directions = ["U", "D", "L", "R"]
    queue = []  # h, w, direction_idx, depth
    current_h, current_w = r_values
    g_h, g_w = g_values
    visited = set()
    queue.append((current_h, current_w, 0))
    while True:
        if len(queue) == 0:
            answer = -1
            break
        current_h, current_w, depth = queue.pop(0)
        if current_h == g_h and current_w == g_w:
            answer = depth
            break
        for direction_inx in range(len(directions)):
            direction = directions[direction_inx]
            if direction == "U":
                next_h = current_h
                while True:
                    next_h -= 1
                    if next_h < 0 or (next_h, current_w) in d_values_set:
                        if next_h + 1 != current_h and (next_h + 1, current_w) not in visited:
                            visited.add((next_h + 1, current_w))
                            queue.append((next_h + 1, current_w, depth + 1))
                        break
            elif direction == "D":
                next_h = current_h
                while True:
                    next_h += 1
                    if next_h >= h_len or (next_h, current_w) in d_values_set:
                        if next_h - 1 != current_h and (next_h - 1, current_w) not in visited:
                            visited.add((next_h - 1, current_w))
                            queue.append((next_h - 1, current_w, depth + 1))
                        break
            elif direction == "L":
                next_w = current_w
                while True:
                    next_w -= 1
                    if next_w < 0 or (current_h, next_w) in d_values_set:
                        if next_w + 1 != current_w and (current_h, next_w + 1) not in visited:
                            visited.add((current_h, next_w + 1))
                            queue.append((current_h, next_w + 1, depth + 1))
                        break
            elif direction == "R":
                next_w = current_w
                while True:
                    next_w += 1
                    if next_w >= w_len or (current_h, next_w) in d_values_set:
                        if next_w - 1 != current_w and (current_h, next_w - 1) not in visited:
                            visited.add((current_h, next_w - 1))
                            queue.append((current_h, next_w - 1, depth + 1))
                        break

    return answer
