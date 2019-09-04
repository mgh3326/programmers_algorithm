def solution(s: str):
    if len(s) == 1:
        return 0
    my_list = []
    for i in s:
        if len(my_list) != 0:
            if my_list[-1] == i:
                my_list.pop()
            else:
                my_list.append(i)
        else:
            my_list.append(i)

    if len(my_list) == 0:
        return 1
    else:
        return 0


print(
    solution("baab")
)
