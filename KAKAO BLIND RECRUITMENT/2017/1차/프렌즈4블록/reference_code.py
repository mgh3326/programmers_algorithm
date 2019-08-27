def pang(m, n, board):
    t_board = []
    for x in range(m):
        t_board.append([])
        for y in range(n):
            t_board[x].append(board[x][y])

    flag = False
    for x in range(m - 1):
        for y in range(n - 1):
            if len(set([board[x][y], board[x][y + 1], board[x + 1][y], board[x + 1][y + 1]])) == 1:
                if board[x][y] != '0':
                    flag = True
                    t_board[x][y] = '0'
                    t_board[x][y + 1] = '0'
                    t_board[x + 1][y] = '0'
                    t_board[x + 1][y + 1] = '0'

    return flag, t_board


def restruct(m, n, board):
    re_board = [''] * m
    for x in range(n):
        ys = ''.join([board[y][x] for y in range(m)]).replace('0', '').zfill(m)
        for y in range(m):
            re_board[y] += ys[y]

    return re_board


def get_num(m, n, board):
    cnt = 0
    for x in range(m):
        for y in range(n):
            if board[x][y] == '0':
                cnt += 1
    return cnt


def solution(m, n, board):
    flag = True
    while flag:
        flag, board = pang(m, n, board)
        board = restruct(m, n, board)

    return get_num(m, n, board)
