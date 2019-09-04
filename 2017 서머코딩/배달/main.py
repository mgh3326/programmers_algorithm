temp_count = 0
answer = 1


def solution(N, road, K):
    global answer
    global temp_count

    # TODO DFS가 아닌 BFS로 짜야한다
    def bfs(n):
        global temp_count
        global answer
        temp_list = [n]
        while True:
            if len(temp_list) == 0:
                break
            n = temp_list.pop(0)
            for _end, _value in my_dict[n]:
                if status_list[_end - 1] == -1 or status_list[_end - 1] > status_list[n - 1] + _value:
                    if status_list[n - 1] + _value <= K:
                        answer += 1
                        my_set.add(_end)
                        status_list[_end - 1] = status_list[n - 1] + _value
                        temp_list.append(_end)

    answer = 1

    my_dict = {}
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for start, end, value in road:
        if start not in my_dict:
            my_dict[start] = []
        if end not in my_dict:
            my_dict[end] = []
        my_dict[start].append((end, value))
        my_dict[end].append((start, value))

    status_list = [-1] * N
    status_list[0] = 0
    my_set = set()
    my_set.add(1)
    bfs(1)
    # BFS로 접근해야되네
    return len(my_set)


print(
    solution(
        5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3
    )
)
# 4
print(
    solution(
        6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]]
        , 4
    )
)
# 4
