def has_valid_pronunciations(value, possible_pronunciations):
    if not value:
        return True
    for i, pronunciation in enumerate(possible_pronunciations):
        if value.startswith(pronunciation):
            if has_valid_pronunciations(value[len(pronunciation):],
                                        possible_pronunciations[:i] + possible_pronunciations[i + 1:]):
                return True
    return False


def solution(babblings):
    possible_pronunciations = ["aya", "ye", "woo", "ma"]
    valid_babblings = 0
    for babble in babblings:
        if has_valid_pronunciations(babble, possible_pronunciations):
            valid_babblings += 1
    return valid_babblings
