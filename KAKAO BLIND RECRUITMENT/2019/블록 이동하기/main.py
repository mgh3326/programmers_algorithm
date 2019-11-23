def solution(board):
    dir_list = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
    ]
    # 회전 -90, +90
    n = len(board)
    answer = 0
    queue = []
    queue.append([0, 0, 0, 1, 0])  # h1,w1,h2,w2,cost
    visit_set = set()
    visit_set.add((0, 0, 0, 1))
    visit_set.add((0, 1, 0, 0))
    while True:
        if len(queue) == 0:
            break
        h1, w1, h2, w2, cost = queue.pop(0)
        if (h1 == n - 1 and w1 == n - 1) or (h2 == n - 1 and w2 == n - 1):
            answer = cost
            break
        for dh, dw in dir_list:
            nh1, nw1, nh2, nw2 = h1 + dh, w1 + dw, h2 + dh, +w2 + dw
            if nh1 >= n or nw1 >= n or nh2 >= n or nw2 >= n or nh1 < 0 or nw1 < 0 or nh2 < 0 or nw2 < 0 or (
                    nh1, nw1, nh2, nw2) in visit_set:
                continue
            visit_set.add((nh1, nw1, nh2, nw2))
            visit_set.add((nh2, nw2, nh1, nw1))
            queue.append([nh1, nw1, nh2, nw2, cost + 1])
        # 회전을 해보도록 하자
        if h1 == h2:
            w_min = min(w1, w2)
            w_max = max(w1, w2)
            nh = h1 + 1
            if nh < n and board[nh][w_min] == 0 and board[nh][w_max] == 0:
                # 1번을 축으로 90 회전
                if (h1, w_min, nh, w_min) not in visit_set:
                    visit_set.add((h1, w_min, nh, w_min))
                    visit_set.add((nh, w_min, h1, w_min))
                    queue.append([h1, w_min, nh, w_min, cost + 1])
                # 2번을 축으로 -90 회전
                if (h1, w_max, nh, w_max) not in visit_set:
                    visit_set.add((h1, w_max, nh, w_max))
                    visit_set.add((nh, w_max, h1, w_max))
                    queue.append([h1, w_max, nh, w_max, cost + 1])
            nh = h1 - 1
            if nh >= 0 and board[nh][w_min] == 0 and board[nh][w_max] == 0:
                # 1번을 축으로 -90 회전
                if (h1, w_min, nh, w_min) not in visit_set:
                    visit_set.add((h1, w_min, nh, w_min))
                    visit_set.add((nh, w_min, h1, w_min))
                    queue.append([h1, w_min, nh, w_min, cost + 1])
                # 2번을 축으로 90 회전
                if (h1, w_max, nh, w_max) not in visit_set:
                    visit_set.add((h1, w_max, nh, w_max))
                    visit_set.add((nh, w_max, h1, w_max))
                    queue.append([h1, w_max, nh, w_max, cost + 1])
        if w1 == w2:
            h_min = min(h1, h2)
            h_max = max(h1, h2)
            nw = w1 + 1
            if nw < n and board[h_min][nw] == 0 and board[h_max][nw] == 0:
                # 1번을 축으로 90 회전
                if (h_min, w1, h_min, nw) not in visit_set:
                    visit_set.add((h_min, w1, h_min, nw))
                    visit_set.add((h_min, nw, h_min, w1))
                    queue.append([h_min, w1, h_min, nw, cost + 1])
                # 2번을 축으로 -90 회전
                if (h_max, w1, h_max, nw) not in visit_set:
                    visit_set.add((h_max, w1, h_max, nw))
                    visit_set.add((h_max, nw, h_max, w1))
                    queue.append([h_max, w1, h_max, nw, cost + 1])
            nw = w1 - 1

            if nw >= 0 and board[h_min][nw] == 0 and board[h_max][nw] == 0:
                # 1번을 축으로 -90 회전
                if (h_min, w1, h_min, nw) not in visit_set:
                    visit_set.add((h_min, w1, h_min, nw))
                    visit_set.add((h_min, nw, h_min, w1))
                    queue.append([h_min, w1, h_min, nw, cost + 1])
                # 2번을 축으로 -90 회전
                if (h_max, w1, h_max, nw) not in visit_set:
                    visit_set.add((h_max, w1, h_max, nw))
                    visit_set.add((h_max, nw, h_max, w1))
                    queue.append([h_max, w1, h_max, nw, cost + 1])
    return answer


print(
    solution([[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]
             )
)
