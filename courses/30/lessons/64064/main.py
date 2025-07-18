import re


def solution(user_id, banned_id):
    answer = 0
    candidates_list = []
    for banned_str in banned_id:
        reg = banned_str.replace("*", "\\w")
        temp_list = []
        for user_idx, user_str in enumerate(user_id):
            if len(banned_str) == len(user_str) and re.match(reg, user_str):
                temp_list.append(user_idx)
        candidates_list.append(temp_list)

    stack = []
    candidates = candidates_list[0]
    answer_set = set()
    for candidate in candidates:
        stack.append((1, set([candidate])))
    while stack:
        depth, candidate_set = stack.pop()
        if depth == len(candidates_list):
            if tuple(sorted(candidate_set)) not in answer_set:
                answer_set.add(tuple(sorted(candidate_set)))
                answer += 1
            continue
        candidates = candidates_list[depth]
        for candidate in candidates:
            if candidate in candidate_set:
                continue
            new_set = set(candidate_set)
            new_set.add(candidate)
            stack.append((depth + 1, new_set))
    return answer
