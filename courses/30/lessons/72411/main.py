import itertools


def solution(orders, course):
    answer = []
    for course_value in course:
        comb_set_list = []
        max_count = 0
        comb_hash = {}
        temp_answer_list = []
        for i in range(len(orders)):
            order = orders[i]
            comb_set = set(itertools.combinations(sorted(order), course_value))
            comb_set_list.append(comb_set)
        for i in range(len(orders)):
            for j in range(i + 1, len(orders)):
                if i == j:
                    continue
                for value in list(comb_set_list[i] & comb_set_list[j]):
                    comb_hash[value] = comb_hash.get(value, 0) + 1
                    if comb_hash[value] > max_count:
                        max_count = comb_hash[value]
                        temp_answer_list = [value]
                    elif comb_hash[value] == max_count:
                        temp_answer_list.append(value)
        answer.append(temp_answer_list)
    result = []
    for values in answer:
        for value in values:
            result.append("".join(value))
    return sorted(result)
