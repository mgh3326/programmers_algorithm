def solution(record):
    answer = []
    user_name_dict = {}
    saved_list = []
    for record_value in record:
        split = record_value.split()
        if split[0] == "Enter":
            user_name_dict[split[1]] = split[2]
            saved_list.append([split[1], split[0]])
        elif split[0] == "Leave":
            saved_list.append([split[1], split[0]])
        elif split[0] == "Change":
            user_name_dict[split[1]] = split[2]
    for saved in saved_list:
        out_str = ""
        user_id, enter_or_leave = saved
        user_name = user_name_dict[user_id]
        out_str += user_name
        if enter_or_leave == "Enter":
            out_str += "님이 들어왔습니다."
        else:
            out_str += "님이 나갔습니다."
        answer.append(out_str)
    return answer


print(
    solution(
        ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
    )
)
