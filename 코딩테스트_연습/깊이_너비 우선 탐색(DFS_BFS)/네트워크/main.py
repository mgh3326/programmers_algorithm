def solution(n, computers):
    def remove_computer(_pop):
        for value in _pop:
            if value in computer_dict:
                temp_pop = computer_dict.pop(value)
                remove_computer(temp_pop)

    answer = 0
    computer_dict = {}
    # Computer dict 만들기
    for idx, computer in enumerate(computers):

        for i in range(n):
            if i == idx:
                continue
            if computer[i] == 1:
                if idx not in computer_dict:
                    computer_dict[idx] = []
                computer_dict[idx].append(i)
    # Computer dict 만들때 아무곳도 못간 애들(갯수 만큼 네트워크 갯수로 볼수 있다.)
    for i in range(n):
        if i not in computer_dict:
            answer += 1
    # Computer dict 의 값을 하나 pop 하여 DFS 를 이용하여 갈수 있는 곳은 모조리 가도록 함(while 문의 반복이 곧 네트워크 값의 증가를 의미함)
    while True:
        if len(computer_dict) == 0:
            break
        key, value_list = computer_dict.popitem()
        pop = value_list
        remove_computer(pop)  # dfs 로 접근했네
        answer += 1
    return answer


print(
    solution(
        3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    )
)
# 2
print(
    solution(
        3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    )
)
# 1
