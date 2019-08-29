def func(num, n):
    if num == 0:
        return "0"
    return_str = ""
    while True:
        if num == 0:
            # return_str = str(num % n) + return_str
            break
        num_n = num % n
        s = ""
        if num_n > 9:
            if num_n == 10:
                s = "A"
            elif num_n == 11:
                s = "B"
            elif num_n == 12:
                s = "C"
            elif num_n == 13:
                s = "D"
            elif num_n == 14:
                s = "E"
            elif num_n == 15:
                s = "F"
        else:
            s = str(num_n)
        return_str = s + return_str
        num //= n
    return return_str


def solution(n, t, m, p):
    answer = ''
    current_index = 1
    for i in range(t * m):
        if len(answer) == t:
            break
        func1 = func(i, n)

        for func_str in func1:
            if len(answer) == t:
                break
            if current_index == p:
                answer += func_str
            current_index += 1
            if current_index == m + 1:
                current_index = 1
        # 각 숫자별로 진수변환을 해주어야겠다
    return answer


n_list = [
    2, 16, 16
]
t_list = [
    4, 16, 16
]
m_list = [
    2, 2, 2
]
p_list = [
    1, 1, 2
]

return_list = [
    "0111",
    "02468ACE11111111",
    "13579BDF01234567"
]
for _input_data in zip(n_list, t_list, m_list, p_list, return_list):
    _0, _1, _2, _3 = _input_data[:-1]
    _r = _input_data[-1]
    print(n_list.index(_0))
    result = solution(_0, _1, _2, _3)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
