def solution(a, b):
    size = len(a)
    answer = 0
    for index in range(size):
        answer += a[index] * b[index]
    return answer
