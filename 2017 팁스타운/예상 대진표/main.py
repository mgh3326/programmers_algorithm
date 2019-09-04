def my_func(num):
    if num % 2 == 1:
        return (num + 1) // 2
    else:
        return num // 2


def solution(n, a, b):
    answer = 1
    while True:
        if abs(b - a) == 1:
            if min(b, a) % 2 == 1:
                break
        answer += 1
        b = my_func(b)
        a = my_func(a)

    return answer


print(solution(8, 4, 7))
