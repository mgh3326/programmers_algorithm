import functools


def solution(arr):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    def lcm(x, y):
        _lcm = (x * y) // gcd(x, y)
        return _lcm

    answer = functools.reduce(lcm, arr)
    return answer
