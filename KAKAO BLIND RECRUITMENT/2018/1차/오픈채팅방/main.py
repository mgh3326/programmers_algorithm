def solution(record: list):
    my_dict = {}
    my_list = []
    for record_value in record:
        split = record_value.split(" ")
        if len(split) == 3:
            is_enter, user_id, name = split
        else:
            is_enter, user_id = split
        if is_enter == "Enter":
            my_dict[user_id] = name
        elif is_enter == "Change":
            my_dict[user_id] = name
        if is_enter == "Enter" or is_enter == "Leave":
            my_list.append((is_enter, user_id))
    answer = []
    for my in my_list:
        my_str = my_dict[my[1]]

        if my[0] == "Enter":
            my_str += "님이 들어왔습니다."

        else:
            my_str += "님이 나갔습니다."
        answer.append(my_str)
    return answer


record_list = [
    ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
]
return_list = [
    ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
]
for _input_data in zip(record_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(record_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
