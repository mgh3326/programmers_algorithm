def is_composite(number):
    """
    This function checks if a number is composite.
    A composite number is a positive integer that has at least one positive divisor other than one or itself.
    In other words, a composite number is any positive integer greater than one that is not a prime number.
    """
    if number < 4:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return True
    return False


def solution(n):
    answer = sum(is_composite(i) for i in range(4, n + 1))
    return answer
