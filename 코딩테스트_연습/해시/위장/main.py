def solution(clothes: list):
    def dfs(n, is_append):
        if n == len(my_dict):

            if is_append == True:
                if len(temp_list) > 0:
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

    answer = 0
    my_dict = {}
    my_list = []
    for clothe in clothes:
        name, kind = clothe
        if kind not in my_dict:
            my_dict[kind] = []
        my_dict[kind].append(name)
    temp_sum = 0
    temp_pro = 1
    for i in my_dict.keys():
        temp_pro *= (len(my_dict[i]) + 1)
    temp_sum = temp_pro - 1
    return temp_sum
    temp_list = []
    dfs(-1, False)
    for mys in my_list:
        temp_list = []
        value = 1
        for my in mys:
            my_ = list(my_dict.keys())[my]
            i = len(my_dict[my_])
            temp_list.append(i)
            value *= i
        answer += value

    return answer


clothes_list = [
    [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]],
    [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]],

    [["yellow_hat", "headgear"]],

]
return_list = [
    5, 3
    , 4
]

for _p, _r in zip(clothes_list, return_list):
    print("index : ", clothes_list.index(_p))
    result = solution(_p)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
