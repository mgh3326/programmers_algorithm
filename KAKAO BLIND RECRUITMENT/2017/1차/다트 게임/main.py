# TODO 레퍼런스 코드처럼 10을 k로 바꿔주면 편하겠다
def solution(dartResult):
    classification_list = ["S", "D", "T"]
    value_list = [0, 0, 0]
    temp_list = []
    current_index = 0
    is_ten = False
    i = dartResult[0]
    idx = 0
    if i.isdigit():
        if i == '1' and dartResult[idx + 1].isdigit():
            is_ten = True

    for idx in range(len(dartResult))[1:]:
        if is_ten == True:
            is_ten = False
            continue
        i = dartResult[idx]
        if i.isdigit():
            if i == '1' and dartResult[idx + 1].isdigit():
                temp_list.append(dartResult[current_index:idx])
                current_index = idx
                is_ten = True
            else:
                temp_list.append(dartResult[current_index:idx])
                current_index = idx
    temp_list.append(dartResult[current_index:])
    for temp_list_index in range(len(temp_list)):
        temp = temp_list[temp_list_index]
        value = 0
        for classification in classification_list:
            if classification in temp:
                temp_index = temp.index(classification)
                value = int(temp[:temp_index])
                value = pow(value, classification_list.index(classification) + 1)
                if temp_index != len(temp) - 1:  # 마지막 인덱스가 아니라면
                    if temp[-1] == "#":
                        value *= -1
                        # if temp_list_index != 0:
                        #     value_list[temp_list_index - 1] *= -1
                    elif temp[-1] == "*":
                        value *= 2
                        if temp_list_index != 0:
                            value_list[temp_list_index - 1] *= 2
                break
        value_list[temp_list_index] = value
    answer = 0
    answer = sum(value_list)

    return answer


dartResult_list = [
    "10S*10D*10T*",
    "1D2S#10S",
    "1D2S0T",
    "1S*2T*3S",
    "1D#2S*3S",
    "1T2D3D#",
    "1D2S3T*"
]

return_list = [
    37,
    9,
    3,
    23,
    5,
    -4,
    59

]
for _input_data in zip(dartResult_list, return_list):
    _0 = _input_data[0]
    _r = _input_data[-1]
    print(dartResult_list.index(_0))
    result = solution(_0)
    print(result)
    print(_r)
    if result == _r:
        print("맞음")
    else:
        print("틀림")
