def hanoi(n, start, arrival):
    if n == 1:
        return [[start, arrival]]
    else:
        other = 6 - start - arrival
        return hanoi(n - 1, start, other) + [[start, arrival]] + hanoi(n - 1, other, arrival)


def solution(n):
    answer = hanoi(n, 1, 3)
    return answer
