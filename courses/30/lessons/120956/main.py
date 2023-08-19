import copy


def has_valid_pronunciations(value, possible_pronunciations):
    idx = 0
    if idx == len(value):
        return True
    current_segment = value[idx:]
    for i, pronunciation in enumerate(possible_pronunciations):
        if current_segment.startswith(pronunciation):
            idx += len(pronunciation)
            deepcopy = copy.deepcopy(possible_pronunciations)
            deepcopy.pop(i)
            if has_valid_pronunciations(value[idx:], deepcopy):
                return True
    return False


def solution(babblings):
    possible_pronunciations = ["aya", "ye", "woo", "ma"]
    valid_babblings = 0
    for babble in babblings:
        if has_valid_pronunciations(babble, copy.deepcopy(possible_pronunciations)):
            valid_babblings += 1
    return valid_babblings
