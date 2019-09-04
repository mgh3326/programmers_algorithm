def solution(N):
    def fibonacci(index):
        if fibonacci_list[index] == -1:
            fibonacci_list[index] = (fibonacci(index - 1) + fibonacci(index - 2))
        return fibonacci_list[index]

    answer = 0
    fibonacci_list = [1, 1, 2, 3, 5, 8, ]
    fibonacci_list.extend([-1] * (N - len(fibonacci_list) + 1))
    answer = fibonacci(N) * 2 + fibonacci(N - 1) * 2

    return answer


print(
    solution(
        5
    )
)
# 26

print(
    solution(
        6
    )
)
# 42
