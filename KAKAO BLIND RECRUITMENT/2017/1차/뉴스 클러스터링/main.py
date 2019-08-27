# TODO set을 사용하면 편하게 할수 있네 레퍼런스 코드를 참고하도록 하자
def solution(str1: str, str2: str):
    str1 = str1.lower()
    str2 = str2.lower()
    count = 0
    my_dict = {}
    str1_len = 0
    str2_len = 0

    for i in range(len(str1) - 1):
        if not str1[i].isalpha():
            continue
        if not str1[i + 1].isalpha():
            continue
        str1_result = str1[i] + str1[i + 1]
        if str1_result in my_dict:
            my_dict[str1_result].append(0)

        else:
            my_dict[str1_result] = [0]
        str1_len += 1
    for i in range(len(str2) - 1):
        if not str2[i].isalpha():
            continue
        if not str2[i + 1].isalpha():
            continue
        str2_result = str2[i] + str2[i + 1]
        if str2_result in my_dict:
            if len(my_dict[str2_result]) > 0:
                my_dict[str2_result].pop()
                count += 1

        str2_len += 1

    answer = 65536
    if not (str1_len == 0 and str2_len == 0):
        answer = int((count / (str1_len + str2_len - count)) * 65536)
    return answer


str1_list = [
    "FRANCE",
    "handshake",
    "aa1+aa2",
    "E=M*C^2"
]
str2_list = [
    "french",
    "shake hands",
    "AAAA12",
    "e=m*c^2"
]
return_list = [
    16384,
    65536,
    43690,
    65536
]
for _input_data in zip(str1_list, str2_list, return_list):
    _0, _1 = _input_data[:-1]
    _r = _input_data[-1]
    print(str1_list.index(_0))
    result = solution(_0, _1)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
