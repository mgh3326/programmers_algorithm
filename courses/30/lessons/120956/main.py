def is_composite_number(n):
    count = 0
    for i in range(n - 1):
        if n % (i + 1) == 0:
            count += 1
            if count >= 2:
                return True
    return False


def solution(n):
    answer = 0
    for i in range(n):
        if is_composite_number(i + 1):
            answer += 1
    return answer
