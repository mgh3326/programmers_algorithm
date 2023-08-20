def solution(board):
    answer = 0
    n = len(board)
    safety_board = [[0] * n for _ in range(n)]
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1), (0, 0)]
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < n:
                        safety_board[ni][nj] = 1
    for i in range(n):
        for j in range(n):
            if safety_board[i][j] == 0:
                answer += 1
    return answer
