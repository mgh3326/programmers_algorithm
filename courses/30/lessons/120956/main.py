def dfs(idx, value, possible_pronunciations):
    if idx == len(value):
        return True
    current_value = value[idx:]
    for possible_pronunciation in possible_pronunciations:
        if current_value.startswith(possible_pronunciation):
            idx += len(possible_pronunciation)
            if dfs(idx, value, possible_pronunciations):
                return True
    return False


def solution(babbling):
    possible_pronunciations = ["aya", "ye", "woo", "ma"]
    result = 0
    for value in babbling:
        idx = 0
        if dfs(idx, value, possible_pronunciations):
            result += 1
    return result
