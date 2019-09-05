def solution(str1, str2):
    set1, list1 = str_to_make_set(str1)
    set2, list2 = str_to_make_set(str2)
    inter_set = set1 & set2
    inter_set_sum = 0
    for i in inter_set:
        inter_set_sum += min(list1.count(i), list2.count(i))
    if len(list1) + len(list2) - inter_set_sum == 0:
        return 65536
    answer = int((65536 * inter_set_sum / (len(list1) + len(list2) - inter_set_sum)))
    return answer


def str_to_make_set(input_str):
    out_set = set()
    out_list = []
    for i in range(len(input_str))[:-1]:
        if input_str[i].isalpha() == False or input_str[i + 1].isalpha() == False:
            continue
        upper_ = input_str[i].upper() + input_str[i + 1].upper()
        out_list.append(upper_)
        out_set.add(upper_)
    return out_set, out_list


print(
    solution(
        "aa1+aa2", "AAAA12"
    )
)
