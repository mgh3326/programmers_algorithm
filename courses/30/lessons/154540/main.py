import sys

sys.setrecursionlimit(10 ** 6)


def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(_h, _w):
        visited.add((_h, _w))
        _total = int(maps[_h][_w])
        for direction_h, direction_w in directions:
            current_h = _h + direction_h
            current_w = _w + direction_w
            if current_h < 0 or current_w < 0 or current_h >= len(maps) or current_w >= len(maps[0]):
                continue
            if (current_h, current_w) in visited or maps[current_h][current_w] == "X":
                continue
            _total += dfs(current_h, current_w)
        return _total

    answer = []
    visited = set()
    for h in range(len(maps)):
        for w in range(len(maps[0])):
            if (h, w) in visited or maps[h][w] == "X":
                continue
            total = dfs(h, w)
            answer.append(total)
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer
