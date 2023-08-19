def is_composite_number(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False


def solution(n):
    answer = sum(is_composite_number(i + 1) for i in range(n))
    return answer
