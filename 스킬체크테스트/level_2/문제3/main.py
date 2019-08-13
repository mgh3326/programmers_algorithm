fibonacci_list = [0, 1, 1, 2, 3, 5]


def fibonacci(n):
    try:
        temp = (fibonacci_list[n - 2])
    except IndexError:
        fibonacci(n - 2)
    try:
        temp = (fibonacci_list[n - 1])
    except IndexError:
        fibonacci(n - 1)
    fibonacci_list.append((fibonacci_list[n - 2] + fibonacci_list[n - 1]) % 1234567)
    return fibonacci_list[n - 2] + fibonacci_list[n - 1]


def solution(n):
    answer = fibonacci(n)
    return answer


n_list = [

    10000
]

return_list = [

    0
]
for p, r in zip(n_list, return_list):
    print(n_list.index(p))
    result = solution(p)
    print(result)
    print(r)
    if result == r:
        print("맞음")
    else:
        print("틀림")
