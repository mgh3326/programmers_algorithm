from collections import deque


def solution(board):
    h_len = len(board)
    w_len = len(board[0])
    obstacles = set()

    for h in range(h_len):
        for w in range(w_len):
            if board[h][w] == "R":
                start = (h, w)
            elif board[h][w] == "G":
                goal = (h, w)
            elif board[h][w] == "D":
                obstacles.add((h, w))

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우
    queue = deque()
    visited = set()

    queue.append((*start, 0))  # (h, w, depth)
    visited.add(start)

    while queue:
        h, w, depth = queue.popleft()
        if (h, w) == goal:
            return depth
        for dx, dy in directions:
            nh, nw = h, w
            while True:
                th, tw = nh + dx, nw + dy
                if not (0 <= th < h_len and 0 <= tw < w_len): break
                if (th, tw) in obstacles: break
                nh, nw = th, tw
            if (nh, nw) not in visited:
                visited.add((nh, nw))
                queue.append((nh, nw, depth + 1))

    return -1
