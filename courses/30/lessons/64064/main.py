import re


def solution(user_id, banned_id):
    answer = 0
    candidates_list = []
    for banned_str in banned_id:
        reg = banned_str.replace("*", "\\w")
        pattern = re.compile("^" + reg + "$")
        temp_list = []
        for user_idx, user_str in enumerate(user_id):
            if len(banned_str) == len(user_str) and pattern.match(user_str):
                temp_list.append(user_idx)
        candidates_list.append(temp_list)

    stack = []
    candidates = candidates_list[0]
    answer_set = set()
    for candidate in candidates:
        stack.append((1, {candidate}))
    while stack:
        depth, candidate_set = stack.pop()
        if depth == len(candidates_list):
            if frozenset(candidate_set) not in answer_set:
                answer_set.add(frozenset(candidate_set))
                answer += 1
            continue
        candidates = candidates_list[depth]
        for candidate in candidates:
            if candidate in candidate_set:
                continue
            stack.append((depth + 1, candidate_set | {candidate}))
    return answer
