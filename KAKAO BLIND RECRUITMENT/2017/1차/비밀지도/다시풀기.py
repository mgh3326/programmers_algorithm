def to_binary_number_str(input_number, n):
    binary_str = ''
    for n_idx in range(n):
        if input_number == 0:
            break
        number_n = input_number % 2
        input_number = input_number // 2
        if number_n == 1:
            binary_str = "#" + binary_str
        else:
            binary_str = " " + binary_str
    for n_idx in range(len(binary_str), n):
        binary_str = " " + binary_str
    return binary_str


def solution(n, arr1, arr2):
    answer = []
    for n_idx in range(n):
        or_number = arr1[n_idx] | arr2[n_idx]
        # 2진수로 변경해줘야겠다.
        binary_number_str = to_binary_number_str(or_number, n)
        answer.append(binary_number_str)
    return answer


print(
    solution(
        5,
        [9, 20, 28, 18, 11],
        [30, 1, 21, 17, 28]
    )
)

print(
    solution(
        6,
        [46, 33, 33, 22, 31, 50],
        [27, 56, 19, 14, 14, 10]
    )
)
