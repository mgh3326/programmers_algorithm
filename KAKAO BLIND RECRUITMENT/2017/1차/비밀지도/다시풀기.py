def to_binaray_number(input_number, n):
    binaray_list = [' '] * n
    for i in range(n):
        if input_number == 0:
            break
        number_n = input_number % 2
        input_number = input_number // 2
        if number_n==1:
            binaray_list[n - i - 1] = "#"

    return binaray_list


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        i_ = arr1[i] | arr2[i]
        number = to_binaray_number(i_, n)
        answer.append(''.join(number))
        # 2진수로 변경해줘야겠다.
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
