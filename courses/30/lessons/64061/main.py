def solution(board, moves):
    box_size = len(board)
    stack = []
    answer = 0
    for move in moves:
        for _i in range(box_size):
            h = _i
            w = move - 1
            value = board[h][w]
            if value > 0:
                if len(stack) > 0 and stack[-1] == value:
                    stack.pop(-1)
                    answer += 2
                else:
                    stack.append(value)
                board[h][w] = 0
                break
    return answer
