import sys

sys.setrecursionlimit(10 ** 6)


def solution(maps):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(_h, _w, path):
        if (_h, _w) in visited or maps[_h][_w] == "X":
            return path
        visited.add((_h, _w))
        temp_list.append(int(maps[_h][_w]))
        for direction_h, direction_w in directions:
            current_h = _h + direction_h
            current_w = _w + direction_w
            if current_h < 0 or current_w < 0 or current_h >= len(maps) or current_w >= len(maps[0]):
                continue
            dfs(current_h, current_w, path + [(current_h, current_w)])

    answer = []
    visited = set()
    for h in range(len(maps)):
        for w in range(len(maps[0])):
            if (h, w) in visited or maps[h][w] == "X":
                continue
            temp_list = []
            dfs(h, w, [(h, w)])
            answer.append(sum(temp_list))
    if len(answer) == 0:
        return [-1]
    answer.sort()
    return answer
