def solution(relation: list):
    def dfs(n, is_append):
        if n + 1 > relation_value_len:
            if is_append == True:
                if len(temp_list) != 0:
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

    # 부분집합을 이용하도록 하자
    relation_value_len = len(relation[0])
    temp_list = []
    my_list = []
    oh_list = []  # 유일성을 맞추는 리스트
    dfs(-1, False)
    answer = 0
    for my in my_list:
        my_dict = {}

        for idx, relation_value_list in enumerate(relation):
            temp_list = []
            for my_value in my:
                temp_list.append(relation_value_list[my_value])
            if tuple(temp_list) in my_dict:
                break
            my_dict[tuple(temp_list)] = 0
            if idx == len(relation) - 1:
                oh_list.append(set(my))
    l = sorted(oh_list)
    for oh in l:
        oh_dict = {}

        is_end = True
        for two_oh in l:
            if two_oh == oh:
                continue
            if oh.issuperset(two_oh):
                is_end = False
                break
        if is_end == True:
            answer += 1
    return answer


relation_list = [
    [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
     ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]],

    [["100", "apeach", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer1", "3"],
     ["400", "con", "computer", "4"], ["500", "muzi", "music2", "3"], ["600", "apeach", "music3", "2"]],

    [["100"], ["100"]]
]

return_list = [
    2
    ,
    1, 0
]
for _input_data in zip(relation_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(relation_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
