import sys

sys.setrecursionlimit(10 ** 6)


def solution(strs, t):
    global answer

    def dfs(current_index, depth):
        global answer
        if current_index == len(t):
            if answer == -1 or answer > depth:
                answer = depth
            return depth
        if answer != -1 and depth >= answer:  # 백트레킹
            return
        if current_index in my_dict:
            temp_min = -1
            for my_str_value in my_dict[current_index]:
                # str_ = t[current_index:current_index + len(my_str_value)]
                # if str_ == my_str_value:
                temp = 0
                if current_index + len(my_str_value) == len(t):
                    temp = dfs(current_index + len(my_str_value), depth + 1)
                else:
                    if dp_list[current_index + len(my_str_value)] > 0:
                        temp = 1 + dp_list[current_index + len(my_str_value)]
                        #TODO current_index + len(my_str_value) 이 값이 끝까지 갈수 있도록 루프문을 돌려줘야한다.
                    elif dp_list[current_index + len(my_str_value)] == 0:
                        temp = dfs(current_index + len(my_str_value), depth + 1)
                if temp_min == -1 or temp < temp_min:
                    temp_min = temp
            return temp_min

    my_dict = {}
    dp_list = [0] * len(t)
    for idx in range(len(t)):
        for my_str in strs:
            if my_str == t[idx:idx + len(my_str)]:
                if idx not in my_dict:
                    my_dict[idx] = []
                my_dict[idx].append(my_str)
    answer = -1
    for i in reversed(range(0, len(t))):
        dfs(i, 0)
        if i == 0:
            break
        dp_list[i] = answer
        answer = -1
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    if answer == -1:
        return -1
    else:
        return answer - 1


print(
    solution(
        ["ba", "na", "n", "a"], "banana"
    )
)
print(
    solution(
        ["app", "ap", "p", "l", "e", "ple", "pp"], "apple"
    )
)

print(
    solution(
        ["ba", "an", "nan", "ban", "n"], "banana"
    )
)
