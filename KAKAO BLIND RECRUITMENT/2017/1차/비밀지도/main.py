def to_binary(input_n, n):
    binary_list = []
    if input_n == 0:
        return [0] * n
    while True:
        if input_n == 1:
            binary_list.insert(0, input_n)
            if len(binary_list) < n:
                temp_list = [0] * (n - len(binary_list))
                temp_list.extend(binary_list)
                binary_list = temp_list

            break

        binary_list.insert(0, input_n % 2)
        input_n = input_n // 2
    return binary_list


def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        result_str = ""
        temp_str = ""
        binary1 = to_binary(arr1[i], n)
        binary2 = to_binary(arr2[i], n)
        for j in range(n):
            if binary1[j] == 1 or binary2[j] == 1:
                if temp_str != "":
                    result_str += temp_str
                    temp_str = ""
                result_str += "#"
            else:
                temp_str += " "
        result_str += temp_str
        answer.append(result_str)

    return answer


n_list = [
    5,
    6
]
arr1_list = [
    [0, 20, 28, 18, 11],
    [46, 33, 33, 22, 31, 50]
]
arr2_list = [
    [0, 1, 21, 17, 28],
    [27, 56, 19, 14, 14, 10]
]
return_list = [
    ["#####", "# # #", "### #", "# ##", "#####"],
    ["######", "### #", "## ##", " #### ", " #####", "### # "]
]
for _input_data in zip(n_list, arr1_list, arr2_list, return_list):
    _0, _1, _2 = _input_data[:-1]
    _r = _input_data[-1]
    print(n_list.index(_0))
    result = solution(_0, _1, _2)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
