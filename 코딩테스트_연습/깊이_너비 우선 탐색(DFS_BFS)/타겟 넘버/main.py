def solution(numbers, target):
    def dfs(n, is_append):
        if n + 1 > len(numbers):
            if is_append == True:
                my_list.append(temp_list.copy())
            return
        if is_append == True:
            temp_list.append(n)
            dfs(n + 1, True)
            dfs(n + 1, False)
            temp_list.remove(n)
        else:
            dfs(n + 1, True)
            dfs(n + 1, False)

    temp_list = []
    my_list = []
    dfs(-1, False)
    answer = 0
    for my in my_list:
        temp_value = 0
        for i in range(len(numbers)):
            if i in my:
                temp_value += numbers[i]
            else:
                temp_value -= numbers[i]
        if temp_value == target:
            answer += 1

    return answer


print(
    solution([1, 1, 1, 1, 1], 3)
)
# 5
